import sys

from twitter.download import *
import yaml

try:
    config_yaml = open("config.yml")
except:
    exit("config.yml file is missing, run setup.py")

CONFIG = yaml.safe_load(config_yaml)


def run(name):
    auth_pair = (None, None) #fill accordingly
    alltweets, outtweets = get_all_tweets(name, CONFIG, auth_pair, False, True)
    if alltweets:
        create_csv(outtweets, name)
        create_csv(alltweets, name, True)
        print("Tweets have been downloaded succesfully")
    else:
        print("No tweets found for user")


if __name__ == "__main__":
    p = ['']
    for i in p:
        print("Downloading " + i)
        run(i)
        print("-"*80)
