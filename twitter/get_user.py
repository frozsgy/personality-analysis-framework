import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

import tweepy

from twitter.secrets import *
from twitter.tweet import *
from twitter.user import *

def get_user(screen_name):

    secret = Secrets()
    
    auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
    auth.set_access_token(secret.access_key, secret.access_secret)
    api = tweepy.API(auth)
    try:
    	user = api.get_user(screen_name)
    	user_return = User(user)
    	return user_return
    except:
    	return False
