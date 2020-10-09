import yaml

from gevent.pywsgi import WSGIServer
from flask import request, json, Flask, jsonify, send_file
from flask_cors import CORS
import tweepy

from web.service import Service
from web.db import DB
from web.plot import plot_ocean
from web.id import PushID

import threading
from main import calculate_vector, cluster, get_ocean

try:
    config_yaml = open("./config.yml")
except:
    exit("config.yml file is missing, run setup.py")

CONFIG = yaml.safe_load(config_yaml)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": CONFIG['url']}})

service = Service(CONFIG)

threads = []


@app.route('/', methods=['GET'])
@app.route('/api/', methods=['GET'])
def _serve():
    try:
        result = {'status': 200, 'url': service.login()}
        return jsonify(result)
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/callback', methods=['GET'])
@app.route('/api/callback', methods=['GET'])
def _callback():
    try:
        db = DB(CONFIG)
        oauth_token = request.args.get('oauth_token')
        oauth_verifier = request.args.get('oauth_verifier')
        auto_share = request.args.get('auto_share')

        auth_pair = service.callback(oauth_token, oauth_verifier)

        auth = tweepy.OAuthHandler(CONFIG["twitter"]["consumer_key"],
                                   CONFIG["twitter"]["consumer_secret"])
        auth.set_access_token(*auth_pair)
        api = tweepy.API(auth)
        me = api.me()
        user_id = me._json['id']
        username = me._json['screen_name']
        total_tweets = me._json['statuses_count']
        if db.check_if_user_exists(user_id) == False:
            db.add_user(user_id, username, auth_pair[0], auth_pair[1], total_tweets)
        else:
            db.update_tokens(user_id, auth_pair[0], auth_pair[1])
        push_id = PushID()
        r_hash = push_id.next_id()
        db.insert_ocean(r_hash, user_id, auto_share == "true")

        j = threading.Thread(target=get_ocean, args=(username, user_id, r_hash))
        threads.append(j)
        j.start()
        q_hash = service.hash(user_id, *auth_pair)
        result = {'status': 200, 'url': "result?hash=" + r_hash +
                  "&auto_share=" + auto_share, 'secret': q_hash, 'hash': r_hash}
        return jsonify(result)
        j.join()

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/result', methods=['GET'])
@app.route('/api/result', methods=['GET'])
def _result():
    try:
        db = DB(CONFIG)
        r_hash = request.args.get('hash')
        auto_share = request.args.get('auto_share')
        status = db.get_status_by_hash(r_hash)
        user_id = db.get_uid_by_hash(r_hash)
        auth_pair = db.get_tokens_by_id(user_id)
        total_tweets = db.get_total_tweets_by_id(user_id)
        if total_tweets < 10 and total_tweets > -1:
            total_tweets = 0
        elif total_tweets > 3200:
            total_tweets = 3200
        response = dict()
        if status == "FINISHED":
            ocean = db.get_ocean_by_hash(r_hash)
            username = db.get_username_by_id(user_id)
            filename = plot_ocean(username, ocean, CONFIG['pwd'], CONFIG['url'], r_hash)
            auto_share_db = db.get_share_by_hash(r_hash)
            if auto_share_db == 1:
                service.share_result(r_hash, *auth_pair)
                db.set_share_by_hash(r_hash)
            response = {'status': 200, 'finished': True, 'hash': r_hash, 'dataSize': total_tweets}
            # db.update_tokens(user_id, "deleted", "deleted")
        else:
            response = {'status': 200, 'finished': False, 'dataSize': total_tweets}
        return jsonify(response)

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/validate', methods=['POST'])
@app.route('/api/validate', methods=['POST'])
def _validate():
    try:
        db = DB(CONFIG)
        r_hash = request.form.get('hash')
        r_secret = request.form.get('secret')
        response = {'status': 500, 'error': 'Exception occurred'}
        if r_hash is not None and r_secret is not None:
            status = db.get_status_by_hash(r_hash)
            user_id = db.get_uid_by_hash(r_hash)
            auth_pair = db.get_tokens_by_id(user_id)
            q_hash = service.hash(user_id, *auth_pair)
            if status == "FINISHED" and q_hash == r_secret:
                survey_status = db.get_survey_by_hash(r_hash) == 1
                response = {'status': 200, 'finished': survey_status}
        return jsonify(response)

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/image', methods=['GET'])
@app.route('/api/image', methods=['GET'])
def _image():
    try:
        r_hash = request.args.get('hash')
        working_directory = CONFIG['pwd']
        return send_file(f'{working_directory}/web/images/{r_hash}.png', mimetype='image/png')

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/questionnaire', methods=['POST'])
@app.route('/api/questionnaire', methods=['POST'])
def _questionnaire():
    try:
        db = DB(CONFIG)
        r_hash = request.form.get('hash')
        r_secret = request.form.get('secret')
        result = {'status': 500, 'error': 'Exception occurred'}
        if r_hash is not None and r_secret is not None:
            status = db.get_status_by_hash(r_hash)
            user_id = db.get_uid_by_hash(r_hash)
            auth_pair = db.get_tokens_by_id(user_id)
            q_hash = service.hash(user_id, *auth_pair)
            if q_hash == r_secret and db.get_survey_by_hash(r_hash) == 0:

                q_responses = []
                for i in range(50):
                    q_id = "q" + str(i)
                    q_r = request.form.get(q_id)
                    q_responses.append(int(q_r))

                hash_id = db.get_id_by_hash(r_hash)
                ocean_results = service.calculate_ocean(q_responses)
                db.save_questionnaire(hash_id, q_responses, ocean_results)
                result = {'status': 200, 'scores': ocean_results}
        return jsonify(result)

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)

@app.route('/stats', methods=['GET'])
@app.route('/api/stats', methods=['GET'])
def _stats():
    try:
        db = DB(CONFIG)
        unique_user_count = db.get_unique_user_count()
        result_count = db.get_result_count()
        questionnaire_count = db.get_questionnaire_count()
        result = {'status': 200, 'stats': {'users': unique_user_count, 'results': result_count, 'questionnaire': questionnaire_count}}
        return jsonify(result)
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/status', methods=['GET'])
@app.route('/api/status', methods=['GET'])
def _status():
    try:
        import subprocess
        processes = ["mariadb", "nginx", "zemberek", "word2vec", "personality"]
        services = dict()
        for process in processes:
            p =  subprocess.Popen(["/usr/bin/systemctl", "is-active",  process], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            output = output.decode('utf-8').split()[0]
            services[process] = output
        result = {'status': 200, 'services': services}
        return jsonify(result)
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)



if __name__ == '__main__':
    try:
        http_server = WSGIServer(('0.0.0.0', 8080), app)
        http_server.serve_forever()
    except KeyboardInterrupt:
        exit()
