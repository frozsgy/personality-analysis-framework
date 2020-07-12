
class Tweet:
    __id = 0
    __time = 0
    __full_text = None
    __rt = False
    __lemma = []
    __normalized_text = None

    def __init__(self):
        pass

    def __init__(self, id, time, tweet, rt):
        self.__id = id
        self.__time = time
        self.__full_text = tweet
        self.__rt = rt

    def get_csv(self):
        return map(str, (self.__id, self.__time, self.__full_text, self.__rt))

    def map_tweet(self, function):
        self.__full_text = function(self.__full_text)
        return self

    def set_normalized_tweet(self, tweet):
        self.__normalized_text == tweet

    def get_normalized_tweet(self):
        return self.__normalized_text

    def get_tweet(self):
        return self.__full_text

    def get_lemma(self):
        return self.__lemma

    def set_lemma(self, lemma):
        self.__lemma = lemma




