import tweepy
import csv

from secrets import *

def get_all_tweets(screen_name, secret):
    
    auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
    auth.set_access_token(secret.access_key, secret.access_secret)
    api = tweepy.API(auth)
   
    alltweets = []  
    
    try:
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200)
    except:
        print(f"Can't get tweets of user {screen_name}")
        exit()
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest)
       
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
     
    with open(f'{screen_name}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

if __name__ == '__main__':
    secret = Secrets()
    name = input("Enter username to download tweets: ")
    get_all_tweets(name, secret)