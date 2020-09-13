import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))
from datetime import datetime
from time import time

import tweepy
import csv

from twitter.tweet import *

def get_all_tweets(screen_name, CONFIG, auth_pair, debug = False, save_raw_data = False, verbose = False):
    
    auth = tweepy.OAuthHandler(CONFIG["twitter"]["consumer_key"], CONFIG["twitter"]["consumer_secret"])
    auth.set_access_token(*auth_pair)
    api = tweepy.API(auth)
   
    alltweets = []  
    
    try:
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, tweet_mode = "extended")
    except:
        print(f"Can't get tweets of user {screen_name}")
        exit()
    
    alltweets.extend(new_tweets)

    if len(alltweets) == 0:
        if save_raw_data is True:
            return (False, False)
        return False
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        # break that allows to download 200 tweets only
        if debug:
            break

        if verbose is True:
            print(f"getting tweets before {oldest}")
        
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest, tweet_mode = "extended")
       
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1

        if verbose is True:
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
    

def create_csv(outtweets, screen_name, r_hash, save_raw_data = False):

    file_name = f'data/tweets/{screen_name}_tweets_{r_hash}.csv'

    now = int(time())
    if save_raw_data is True:
        file_name = f'data/tweets/raw/{screen_name}_tweets_{r_hash}_{now}.csv'
            
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