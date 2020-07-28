import os 

from gensim.test.utils import datapath
from gensim.models import KeyedVectors

dir_path = os.path.dirname(os.path.realpath(__file__))

wv = KeyedVectors.load_word2vec_format(datapath(dir_path + "/" + "wikipedia-vector.bin"), binary=True)

while True:
	w = input("Enter word: ")
	print(wv[w])


