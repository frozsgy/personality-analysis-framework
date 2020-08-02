import sys

from twitter.download import *


def run(name):
    alltweets, outtweets = get_all_tweets(name, False, True)
    if alltweets:
        create_csv(outtweets, name)
        create_csv(alltweets, name, True)
        print("Tweets have been downloaded succesfully")
    else :
        print("No tweets found for user")


if __name__ == "__main__":
    """args = sys.argv
    if len(args) > 1 :
        username = args[1]
    else :
        name = input("Enter username to download tweets: ")
    run(username)"""

    p = ['']
    for i in p:
        print("Downloading " + i)
        run(i)
        print("-"*80)
