from twitter.download import *


name = input("Enter username to download tweets: ")
outtweets = get_all_tweets(name)
create_csv(outtweets, name)
print("Tweets have been downloaded succesfully")