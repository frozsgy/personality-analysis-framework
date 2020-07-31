import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))
from datetime import datetime

import tweepy
import csv

from twitter.secrets import *
from twitter.tweet import *

def get_all_tweets(screen_name, debug = False, save_raw_data = False):

    secret = Secrets()
    
    auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
    auth.set_access_token(secret.access_key, secret.access_secret)
    api = tweepy.API(auth)
   
    alltweets = []  
    
    try:
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, tweet_mode = "extended")
    except:
        print(f"Can't get tweets of user {screen_name}")
        exit()
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        # break that allows to download 200 tweets only
        if debug:
            break
        print(f"getting tweets before {oldest}")
        
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest, tweet_mode = "extended")
       
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    

    print(f"Total number of tweets downloaded: {len(alltweets)}")

    intweets = []
    outtweets = []

    for tweet in alltweets:

        is_rt = False
        try: 
            tweet.retweeted_status
            is_rt = True
        except:
            pass

        t_o = Tweet(tweet.id_str, tweet.created_at, tweet.full_text, is_rt)
        intweets.append(t_o)

        #if tweet.in_reply_to_status_id is None and is_rt is False:
        if is_rt is False:
            t = Tweet(tweet.id_str, tweet.created_at, tweet.full_text, is_rt)
            outtweets.append(t)
            
    print(f"Total number of tweets to process: {len(outtweets)}")

    if save_raw_data is True:
        return (intweets, outtweets)
    return outtweets
    

def create_csv(outtweets, screen_name, save_raw_data = False):

    file_name = f'data/tweets/{screen_name}_tweets.csv'

    if save_raw_data is True:
        file_name = f'data/tweets/raw/{screen_name}_tweets.csv'
            
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","full_text", "is_rt"])
        for tweet in outtweets:
            writer.writerow(tweet.get_csv())

def read_csv(screen_name):
    outtweets = []
    with open(f'data/tweets/{screen_name}_tweets.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for line in reader:
            line[1] = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
            t = Tweet(*line)
            outtweets.append(t)
    return outtweets