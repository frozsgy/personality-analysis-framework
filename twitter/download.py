import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

import tweepy
import csv

from twitter.secrets import *
from twitter.tweet import *

def get_all_tweets(screen_name, debug = False):

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
    outtweets = []

    for tweet in alltweets:
        if tweet.in_reply_to_status_id and tweet.retweeted == False:
            t = Tweet(tweet.id_str, tweet.created_at, tweet.full_text, tweet.retweeted)
            outtweets.append(t)
    print(f"Total number of tweets to process: {len(outtweets)}")
    return outtweets
    

def create_csv(outtweets, screen_name):
    with open(f'{screen_name}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","full_text", "is_rt"])
        for tweet in outtweets:
            writer.writerow(tweet.get_csv())


if __name__ == '__main__':
    name = input("Enter username to download tweets: ")
    outtweets = get_all_tweets(name)
    create_csv(outtweets, name)