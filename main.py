import sys
import re

import numpy as np
from sklearn.preprocessing import KBinsDiscretizer


import json
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import twitter.download
import utils.preprocess
import zemberek
from vector import vector

def run(username, debug = False):
    # Data Collection
    # download.py

    all_tweets = twitter.download.get_all_tweets(username, debug)

    # Data Preprocess

    ## Preprocess
    ## preprocess.py
    preprocessed = [tweet.map_tweet(utils.preprocess.preprocess) for tweet in all_tweets]

    ## Normalization
    ## normalize.py
    normalized = []
    for tweet in preprocessed:
        try :
            lang_id = zemberek.find_lang_id(tweet.get_tweet())
            if lang_id == "tr":
                # continue, tweet is turkish
                n_response = zemberek.normalize(tweet.get_tweet())
                if n_response.normalized_input:
                    tweet.set_normalized_tweet(n_response.normalized_input)
                    normalized.append(tweet)
                else:
                    # not sure if raising an error will cause the halting of the app, if that's the case, we can use a simple print for debugging purposes.
                    raise AttributeError('Problem normalizing input : ' + n_response.error)
            else :
                # do not handle, tweet is turkish
                pass
        except zemberek.grpc._channel._InactiveRpcError:
            print("Cannot communicate with Zemberek, exiting while normalizing.")
            exit()

    ## Lemmatization
    ## normalize.py

    for tweet in normalized:
        try:
            analysis_result = zemberek.analyze(tweet.get_normalized_tweet())
            tweet_lemmas = []
            tweet_pos = []
            tweet_plural = 0
            tweet_words = 0
            tweet_full_stop = 0
            tweet_unknown = 0
            plural_regex = r"A[1-3]pl"
            # print(tweet.get_normalized_tweet())
            # print(len(tweet.get_normalized_tweet().split()))
            for a in analysis_result.results:
                best = a.best
                lemmas = ""
                for l in best.lemmas:
                    if l != "UNK":
                        tweet_lemmas.append(l)
                        tweet_pos.append(best.pos)
                    else :
                        tweet_unknown += 1
                    if re.search(plural_regex, best.analysis, flags=re.S) is not None:
                        tweet_plural += 1
                if a.token == ".":
                    tweet_full_stop += 1
                tweet_words += 1

            for i in tweet_pos:
                tweet.add_pos(i)
            tweet.set_pos("Plur", tweet_plural)
            tweet.set_pos("Word", tweet_words)
            tweet.set_pos("Fstop", tweet_full_stop)
            tweet.set_pos("Inc", tweet_unknown)
            tweet.set_lemma(set(tweet_lemmas))

        except zemberek.grpc._channel._InactiveRpcError:
            print("Cannot communicate with Zemberek, exiting while analyzing.")
            exit()


    # Vector Construction

    for tweet in normalized:
        v = vector.Vector()
        v.set_vector(tweet)
        tweet.set_vector(v)



    ## Feature Extraction

    ## Feature Reduction

    ## Normalization

    sum_vector = np.array([0] * 20)

    sum_lemmas = []

    for tweet in normalized:
        pass
        print("-" * 80)
        print(list(tweet.get_csv()))
        print(tweet.get_normalized_tweet())
        lemma_list = list(tweet.get_lemma())
        sum_lemmas += lemma_list
        print(lemma_list)
        print(tweet.get_pos())
        print(tweet.get_vector().get_vector())
        v = np.array(tweet.get_vector().get_vector())
        sum_vector = np.add(sum_vector, v)
    
    sum_transformed = sum_vector.reshape(-1, 1)

    print(sum_transformed.reshape(1, 20))
    
    normalized = KBinsDiscretizer(n_bins=[4], encode='ordinal').fit(sum_transformed).transform(sum_transformed)

    normalized = normalized/4.

    print(normalized.reshape(1, 20))

    print(sum_lemmas)


    cv = CountVectorizer(max_features = 20, ngram_range = (1, 1), max_df = 0.8)
    top_words = []

    try:
        word_count_vector = cv.fit_transform(sum_lemmas)
        tfidf_transformer = TfidfTransformer(smooth_idf = True, use_idf = True)
        tfidf_transformer.fit(word_count_vector)

        count_vector = cv.transform(sum_lemmas)
        tf_idf_vector = tfidf_transformer.transform(count_vector)

        top_words = cv.get_feature_names()

    except Exception as e:
        print("error accured")



    base_url = "http://127.0.0.1:5000/word2vec?word="

    vector_ = np.array([0] * 38)

    for word in top_words:
        link = base_url + word
        req = requests.get(link)
        try:
            v = req.json()['word2vec'][0]
            if v == '':
                v = [0] * 38
            v_np = np.array(v)
            vector_ = np.add(vector_, v_np)
        except:
            pass
    vv = vector_.tolist()
    print(vv)
    print(normalized.reshape(1, 20).tolist())

    all_vector = vv + normalized.reshape(1, 20).tolist()[0]

    print(all_vector)






    ## TF-IDF Weighting and Word2Vec based Word Embedding

    ## Composition of Extracted Features and Word2Vec Vectors

    # Clustering


if __name__ == '__main__':
    debugging = False
    args = sys.argv
    if len(args) > 1 :
        username = args[1]
        if "--debug" in args:
            debugging = True
    else :
        username = input("Enter username: ")
    run(username, debugging)