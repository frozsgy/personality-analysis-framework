
class User:
    __username = ""
    __created_at = None
    __id = 0
    __following_count = 0
    __follower_count = 0
    __like_count = 0
    __retweet_count = 0
    __tweet_count = 0
    __location = None
    __description = None
    __has_default_profile_pic = True
    __has_extended_profile = False
    __has_background = False


    def __init__(self):
        pass

    def __init__(self, obj):
        json = obj._json
        self.__created_at = json.get('created_at', None)
        self.__id = json.get('id', None)
        self.__username = json.get('screen_name', None)
        self.__following_count = json.get('friends_count', None)
        self.__follower_count = json.get('followers_count', None)
        self.__like_count = json.get('favourites_count', None)
        # self.__retweet_count = json.get(, None)
        self.__tweet_count = json.get('statuses_count', None)
        self.__location = json.get('location', None)
        self.__description = json.get('description', None)
        self.__has_default_profile_pic = json.get('default_profile_image', None)
        self.__has_extended_profile = json.get('has_extended_profile', None)
        self.__has_background = json.get('profile_use_background_image', None)


