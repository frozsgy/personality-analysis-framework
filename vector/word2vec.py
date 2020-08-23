import os 

import numpy as np

from gensim.test.utils import datapath
from gensim.models import KeyedVectors

from gevent.pywsgi import WSGIServer
from flask import request, json, Flask, jsonify

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

word_vector = KeyedVectors.load_word2vec_format(datapath(dir_path + "/" + "wikipedia-vector.bin"), binary = True)

@app.route('/word2vec', methods=['GET'])
def _serve():
    try:
        word = request.args.get('word')
        if word is None or len(word.strip()) == 0:
            return "These aren't the droids you're looking for."
        else :
            vector = word_vector[word]
            vector = vector.tolist()
            result = {'word2vec': vector}
            return jsonify(result)
    except KeyError:
        result = {'word2vec': [""]}
        return jsonify(result)
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    try:
        print("Starting Word2Vec server")
        # for using in development server.
        # app.run(debug=True, host='0.0.0.0', port=5000)
        # for using in production server.
        http_server = WSGIServer(('0.0.0.0', 5000), app)
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting Word2Vec server")
        exit()
