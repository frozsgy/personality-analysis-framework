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
CORS(app)

service = Service(CONFIG)
db = DB()

threads = []


@app.route('/', methods=['GET'])
def _serve():
    try:
        result = {'status': 200, 'url': service.login()}
        return jsonify(result)
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/callback', methods=['GET'])
def _callback():
    try:
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
        if db.check_if_user_exists(user_id) == False:
            db.add_user(user_id, username, auth_pair[0], auth_pair[1])
        else:
            db.update_tokens(user_id, auth_pair[0], auth_pair[1])
        push_id = PushID()
        r_hash = push_id.next_id()
        db.insert_ocean(r_hash, user_id, auto_share)

        j = threading.Thread(target=get_ocean, args=(username, user_id, r_hash))
        threads.append(j)
        j.start()
        result = {'status': 200, 'url': "result?hash=" + r_hash + "&auto_share=" + auto_share}
        return jsonify(result)
        j.join()

    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/result', methods=['GET'])
def _result():
    try:
        r_hash = request.args.get('hash')
        auto_share = request.args.get('auto_share')
        status = db.get_status_by_hash(r_hash)
        user_id = db.get_uid_by_hash(r_hash)
        auth_pair = db.get_tokens_by_id(user_id)
        total_tweets = service.get_total_tweets(*auth_pair)
        if total_tweets < 10:
            total_tweets = 0
        elif total_tweets > 3200:
            total_tweets = 3200
        response = dict()
        if status == "FINISHED":
            ocean = db.get_ocean_by_hash(r_hash)
            username = db.get_username_by_id(user_id)
            filename = plot_ocean(username, ocean, CONFIG['pwd'], CONFIG['url'], r_hash)
            if auto_share == "true":
                service.share_result(r_hash, *auth_pair)
            response = {'status': 200, 'finished': True, 'hash': r_hash, 'dataSize': total_tweets}
        else:
            response = {'status': 200, 'finished': False, 'dataSize': total_tweets}
        return jsonify(response)
        
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/image', methods=['GET'])
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
def _questionnaire():
    try:
        r_hash = request.form.get('hash')
        r_id = request.form.get('id')
        # -- TODO --
        # check if id matches hash
        q_responses = []
        for i in range(50):
            q_id = "q" + str(i)
            q_r = request.form.get(q_id)
            q_responses.append(int(q_r))

        e = 20 + q_responses[0] - q_responses[5] + q_responses[10] - q_responses[15] + q_responses[20] - q_responses[25] + q_responses[30] - q_responses[35] + q_responses[40] - q_responses[45]
        a = 14 - q_responses[1] + q_responses[6] - q_responses[11] + q_responses[16] - q_responses[21] + q_responses[26] - q_responses[31] + q_responses[36] + q_responses[41] + q_responses[46]
        c = 14 + q_responses[2] - q_responses[7] + q_responses[12] - q_responses[17] + q_responses[22] - q_responses[27] + q_responses[32] - q_responses[37] + q_responses[42] + q_responses[48]
        n = 38 - q_responses[3] + q_responses[8] - q_responses[13] + q_responses[18] - q_responses[23] - q_responses[28] - q_responses[33] - q_responses[38] - q_responses[43] - q_responses[48]
        o = 8 + q_responses[4] - q_responses[9] + q_responses[14] - q_responses[19] + q_responses[24] - q_responses[29] + q_responses[34] + q_responses[39] + q_responses[44] + q_responses[49]

        # -- TODO --
        # save results to db
        # 50 questions on table: result_id, int[50], ocean

        result = {'status': 200, 'scores': {'o': o/40, 'c': c/40, 'e': e/40, 'a': a/40, 'n': n/40}}
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
