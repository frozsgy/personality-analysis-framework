# Personality Analysis Framework 

This framework allows users who tweet in Turkish to get an estimation of their Big Five OCEAN Personality scores via their tweets.  

## Academic Background

For academic background of this framework, please refer to [Clustering based Personality Prediction on Turkish Tweets](https://ieeexplore.ieee.org/abstract/document/9073214) by Tutaysalgir, E., Karagoz, P. and Toroslu, I.H., 2019, August. 

## Installation

Please refer to [INSTALL.md](INSTALL.md)

## Requirements

* Python 3.8
* Java 8


For a list of required Python libraries, refer to [requirements.txt](requirements.txt).


## Services List

This framework uses 4 services to run properly. Namely,

1. [Zemberek](https://github.com/ahmetaa/zemberek-nlp) service
2. Word2Vec service
3. Backend REST service via Flask
4. Frontend service via React

### Zemberek Service

Zemberek provides the NLP functionalities for the framework. The communication between the framework and Zemberek is achieved through gRPC. 

To run Zemberek service, you can use ```run_zemberek.sh```.


### Word2Vec service

Word2Vec service provides an API to get Word2Vec representations of words. You can use ```run_word2vec.sh``` to run the service.

### Backend REST service via Flask

The backend of this project relies on a RESTful API to allow any frontend or application to make requests and get responses from it. To achieve this, we use Flask, which has a very simple but powerful interface. 

This service is by nature multithreaded, and it spawns a new thread for every new vector calculation request to handle multiple users at a time. If you expect a huge number of users at the same time, it might be useful to use autoscaling solutions.

### Frontend service via React

The frontend is purely for aesthetics, and it is extremely under-developed. As long as making the proper REST requests, any frontend should work just fine.


## Command Line Usage

Even though this framework is designed as a web tool, it is possible to use this through a terminal window as well. In order to do so, follow these steps after installation:

1. Run Zemberek and Word2Vec services.
2. Fill in ```auth_pair``` in ```main.py``` with your credentials.
3. Run ```python main.py username``` if you want to give username as an argument, or ```python main.py``` to enter username when asked.
4. You will receive the predicted OCEAN score in the terminal.

## Reading from a CSV file

It is possible to download tweets of a user and use this csv file for the vector construction. In order to do so, do the following steps:
1. Fill in ```auth_pair``` in ```download-tweets.py``` with your credentials.
2. Download tweets of a user via ```python download-tweets.py```. This will save the tweets in the ```data/tweets``` folder.
3. Run the vector constructor via ```python main.py username --file``` arguments. This will read the tweets from the csv file instead of downloading them from scratch. 

This method was implemented to avoid burning out the Twitter API for recurrent downloads.
