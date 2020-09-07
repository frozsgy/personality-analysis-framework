import yaml

from gevent.pywsgi import WSGIServer
from flask import request, json, Flask, jsonify
import tweepy

from web.service import Service
from web.db import DB

import threading
from main import calculate_vector, cluster, get_ocean

try:
    config_yaml = open("./config.yml")
except:
    exit("config.yml file is missing, run setup.py")

CONFIG = yaml.safe_load(config_yaml)

app = Flask(__name__)

service = Service(CONFIG)
db = DB()

threads = []

@app.route('/', methods=['GET'])
def _serve():
    try:
        r = "<br /><br /><center>"
        r += "<a href='" + service.login() + "' target='_self'>click here to auth</a>"
        r += "</center>"
        return r
    except BaseException as e:
        print(e)
        return "error"


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
        link = "<a href='http://localhost:8080/result?id="+str(user_id)+"&hash=" + service.hash(user_id, auth_pair[0], auth_pair[1]) + "'>clikc here</a>"
        
        return "downloading tweets " + link
        j.join()
        
    except BaseException as e:
        print(e)
        return "error occurred"


@app.route('/result', methods=['GET'])
def _result():
    try:
        uid = request.args.get('id')
        u_hash = request.args.get('hash')
        auth_pair = db.get_tokens_by_id(uid)
        calculated_hash = service.hash(uid, auth_pair[0], auth_pair[1])
        if u_hash == calculated_hash:
            ocean = db.get_ocean_by_id(uid)[0]
            return "OCAEN: " + ' '.join(map(str, ocean))
        else :
            return "error"
        
    except BaseException as e:
        print(e)
        return "error occurred"

if __name__ == '__main__':
    try:
        http_server = WSGIServer(('0.0.0.0', 8080), app)
        http_server.serve_forever()
    except KeyboardInterrupt:
        exit()
