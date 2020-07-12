import sys

import twitter.download
import utils.preprocess
import zemberek.normalize

def run(username):
    # Data Collection
    # download.py

    all_tweets = twitter.download.get_all_tweets(username)

    # Data Preprocess

    ## Preprocess
    ## preprocess.py
    preprocessed = [tweet.map_tweet(utils.preprocess.preprocess) for tweet in all_tweets]

    ## Normalization
    ## normalize.py
    normalized = []
    for tweet in preprocessed:
        try :
            lang_id = zemberek.normalize.find_lang_id(tweet.get_tweet())
            if lang_id == "tr":
                # continue, tweet is turkish
                n_response = zemberek.normalize.normalize(tweet.get_tweet())
                if n_response.normalized_input:
                    tweet.set_normalized_tweet(n_response.normalized_input)
                    normalized.append(tweet)
                else:
                    # not sure if raising an error will cause the halting of the app, if that's the case, we can use a simple print for debugging purposes.
                    raise AttributeError('Problem normalizing input : ' + n_response.error)
            else :
                # do not handle, tweet is turkish
                pass
        except zemberek.normalize.grpc._channel._InactiveRpcError:
            print("Cannot communicate with Zemberek, exiting.")
            exit()

    ## Lemmatization
    ## normalize.py

    for tweet in normalized:
        try:
            analysis_result = zemberek.normalize.analyze(tweet.get_tweet())
            tweet_lemmas = []
            for a in analysis_result.results:
                best = a.best
                lemmas = ""
                for l in best.lemmas:
                    tweet_lemmas.append(l)
                    lemmas = lemmas + " " + l
                    #print("Word = " + a.token + ", Lemmas = " + lemmas + ", POS = [" + best.pos + "], Full Analysis = {" + best.analysis + "}")
            tweet.set_lemma(set(tweet_lemmas))

        except zemberek.normalize.grpc._channel._InactiveRpcError:
            print("Cannot communicate with Zemberek, exiting.")
            exit()

    for tweet in normalized:
        pass
        print("-" * 80)
        print(list(tweet.get_csv()))
        print(list(tweet.get_lemma()))

    # Vector Construction

    ## Feature Extraction

    ## Feature Reduction

    ## Normalization

    ## TF-IDF Weighting and Word2Vec based Word Embedding

    ## Composition of Extracted Features and Word2Vec Vectors

    # Clustering


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1 :
        username = args[1]
    else :
        username = input("Enter username: ")
    run(username)