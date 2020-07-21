import sys
import re

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


    for tweet in normalized:
        pass
        print("-" * 80)
        print(list(tweet.get_csv()))
        print(tweet.get_normalized_tweet())
        print(list(tweet.get_lemma()))
        print(tweet.get_pos())
        print(tweet.get_vector().get_vector())




    ## Feature Extraction

    ## Feature Reduction

    ## Normalization

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