import tweepy
import hashlib

class Service:

    __consumer_key = None
    __consumer_secret = None
    __callback_url = None

    def __init__(self, CONFIG):
        self.__consumer_key = CONFIG['twitter']['consumer_key']
        self.__consumer_secret = CONFIG['twitter']['consumer_secret']
        self.__callback_url = CONFIG['twitter']['callback_url']

    def login(self):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret, self.__callback_url)

        try:
            redirect_url = auth.get_authorization_url()
            return redirect_url
        except tweepy.TweepError:
            print('Error! Failed to get request token.')

    def callback(self, token, verifier):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret, self.__callback_url)
        auth.request_token = {'oauth_token': token,
                              'oauth_token_secret': verifier}

        try:
            return auth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error! Failed to get access token.')

    def verify(self, token, secret):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret, self.__callback_url)
        auth.set_access_token(token, secret)
        api = tweepy.API(auth)
          
        if api.verify_credentials() == False: 
            return False
        else: 
            return True

    def get_total_tweets(self, token, secret):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret, self.__callback_url)
        auth.set_access_token(token, secret)
        api = tweepy.API(auth)
        user_data = api.me()._json
        total_tweets = user_data.get('statuses_count', 0)
        return total_tweets
