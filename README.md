# Personality Analysis Framework 

This framework allows users who tweet in Turkish to get an estimation of their Big Five OCEAN Personality scores via their tweets.  

## Academic Background

For academic background of this framework, please refer to [Clustering based Personality Prediction on Turkish Tweets](https://ieeexplore.ieee.org/abstract/document/9073214) by Tutaysalgir, E., Karagoz, P. and Toroslu, I.H., 2019, August. 

## Installation

Please refer to [INSTALL.md](INSTALL.md)

## Requirements

* Python
* Java 


For a list of required Python libraries, refer to [requirements.txt](requirements.txt).

## Usage
1. Run the Python script either with ```python main.py username``` for giving username as an argument, or ```python main.py``` for entering username when asked
2. ```python main.py username --debug``` downloads only the recent 200 tweets to allow faster debugging.
-- TODO --

## Reading from a CSV file

It is possible to download tweets of a user and use this csv file for the vector construction. In order to do so, do the following steps:
1. Download tweets of a user via ```python download-tweets.py```. This will save the tweets in the ```data/tweets``` folder.
2. Run the vector constructor via ```python main.py username --file``` arguments. This will read the tweets from the csv file instead of downloading them from scratch. 

This method was implemented to avoid burning out the Twitter API for recurrent downloads.


