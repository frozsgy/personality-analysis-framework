import tweepy
import hashlib

class Service:

    __consumer_key = None
    __consumer_secret = None
    __callback_url = None
    __working_dir = None
    __url = None

    def __init__(self, CONFIG):
        self.__consumer_key = CONFIG['twitter']['consumer_key']
        self.__consumer_secret = CONFIG['twitter']['consumer_secret']
        self.__callback_url = CONFIG['twitter']['callback_url']
        self.__working_dir = CONFIG['pwd']
        self.__url = CONFIG['url']

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

    def share_result(self, r_hash, token, secret):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret, self.__callback_url)
        auth.set_access_token(token, secret)
        api = tweepy.API(auth)
        image_path = f'{self.__working_dir}/web/images/{r_hash}.png'
        status = "Tweetlerime göre kişilik analimizi yaptırdım! Sen de yaptırmak istersen: " + self.__url + "\n#TweetKişiliğim @TweetKisiligim"
        api.update_with_media(image_path, status)

    def hash(self, uid, token, secret):
        phrase = "id={}&tk={}&sc={}".format(uid, token, secret) 
        return hashlib.sha256(phrase.encode()).hexdigest()

    def calculate_ocean(self, q_responses):
        e = 20 + q_responses[0] - q_responses[5] + q_responses[10] - q_responses[15] + q_responses[20] - q_responses[25] + q_responses[30] - q_responses[35] + q_responses[40] - q_responses[45]
        a = 14 - q_responses[1] + q_responses[6] - q_responses[11] + q_responses[16] - q_responses[21] + q_responses[26] - q_responses[31] + q_responses[36] + q_responses[41] + q_responses[46]
        c = 14 + q_responses[2] - q_responses[7] + q_responses[12] - q_responses[17] + q_responses[22] - q_responses[27] + q_responses[32] - q_responses[37] + q_responses[42] + q_responses[48]
        n = 38 - q_responses[3] + q_responses[8] - q_responses[13] + q_responses[18] - q_responses[23] - q_responses[28] - q_responses[33] - q_responses[38] - q_responses[43] - q_responses[48]
        o = 8 + q_responses[4] - q_responses[9] + q_responses[14] - q_responses[19] + q_responses[24] - q_responses[29] + q_responses[34] + q_responses[39] + q_responses[44] + q_responses[49]
        return {'o': o/40, 'c': c/40, 'e': e/40, 'a': a/40, 'n': n/40}
