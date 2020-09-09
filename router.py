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
        db.insert_ocean(r_hash, user_id)

        j = threading.Thread(target=get_ocean, args=(username, user_id, r_hash))
        threads.append(j)
        j.start()
        result = {'status': 200, 'url': "result?hash=" + r_hash}
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
        status = db.get_status_by_hash(r_hash)
        response = dict()
        if status == "FINISHED":
            ocean = db.get_ocean_by_hash(r_hash)
            user_id = db.get_uid_by_hash(r_hash)
            username = db.get_username_by_id(user_id)
            filename = plot_ocean(username, ocean, CONFIG['pwd'], CONFIG['url'], r_hash)
            response = {'status': 200, 'finished': True, 'hash': r_hash}
        else:
            response = {'status': 200, 'finished': False}
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


if __name__ == '__main__':
    try:
        http_server = WSGIServer(('0.0.0.0', 8080), app)
        http_server.serve_forever()
    except KeyboardInterrupt:
        exit()
