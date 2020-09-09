import yaml

from gevent.pywsgi import WSGIServer
from flask import request, json, Flask, jsonify, send_file
from flask_cors import CORS
import tweepy

from web.service import Service
from web.db import DB
from web.plot import plot_ocean

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

        auth = tweepy.OAuthHandler(CONFIG["twitter"]["consumer_key"], CONFIG["twitter"]["consumer_secret"])
        auth.set_access_token(*auth_pair)
        api = tweepy.API(auth)
        me = api.me()
        user_id = me._json['id']
        username = me._json['screen_name']
        if db.check_if_user_exists(user_id) == False:
            db.add_user(user_id, user_id, auth_pair[0], auth_pair[1])
        else:
            db.update_tokens(user_id, auth_pair[0], auth_pair[1])
       
        j = threading.Thread(target=get_ocean, args=(username, user_id))
        threads.append(j)
        j.start()
        result = {'status': 200, 'url': "result?id="+str(user_id)+"&hash=" + service.hash(user_id, auth_pair[0], auth_pair[1])}
        return jsonify(result)
        j.join()
        
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)


@app.route('/result', methods=['GET'])
def _result():
    try:
        uid = request.args.get('id')
        u_hash = request.args.get('hash')
        auth_pair = db.get_tokens_by_id(uid)
        calculated_hash = service.hash(uid, auth_pair[0], auth_pair[1])
        if u_hash == calculated_hash:
            try:
                status = db.get_status_by_id(uid)[0]
                response = dict()
                if status[0] == "FINISHED":
                    ocean = db.get_ocean_by_id(uid)[0]
                    response = {'status': 200, 'finished': True, 'score': {'o': ocean[0], 'c': ocean[1], 'e': ocean[2], 'a': ocean[3], 'n': ocean[4]}}
                else:
                    response = {'status': 200, 'finished': False}
                return jsonify(response)
            except:
                result = {'status': 500, 'error': 'Exception occurred'}
                return jsonify(result)
        else :
            result = {'status': 500, 'error': 'Exception occurred'}
            return jsonify(result)
        
    except BaseException as e:
        print(e)
        result = {'status': 500, 'error': 'Exception occurred'}
        return jsonify(result)

@app.route('/image', methods=['GET'])
def _image():
    try:
        username = request.args.get('username')
        ocean = []
        for personality_type in "ocean":
            ocean.append(float(request.args.get(personality_type)))
        filename = plot_ocean(username, ocean, CONFIG['pwd'], CONFIG['url'])
        return send_file(filename, mimetype='image/png')

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
