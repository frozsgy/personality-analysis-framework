# Installation Manual for the Personality Analysis Framework

## Creating config.yml 

Use ```setup.py``` to generate the configuration file, ```config.yml```. After training the Word2Vec model, you need to run ```config_boundaries.sh``` to generate boundary values for the normalization process. This updates the ```config.yml``` with accordance to these values and it is crucial for the following steps.

## Training Phase

### Training Word2Vec Model

In order to get Word2Vec representations properly, you need to train the Word2Vec library using ```train_model.sh```. This step uses the Wikipedia archive for Turkish language to create a vector space to represent words.

### Acquiring Ground Truths

You need to acquire OCEAN scores for your ground truth users. You may do it with a questionnaire, or other methods. We do not provide a concrete code block for this step, since it may vary vastly.

You also need to create the vector representation of your ground truth users. -- TODO --

### Training SciKit Model

After acquiring the ground truth vectors, you need to train your machine learning model to use with the system. -- TODO -- Save model using pickle or joblib.

## Creating Services

This framework uses 4 services to run properly. Namely,

1. [Zemberek](https://github.com/ahmetaa/zemberek-nlp) service
2. Word2Vec service
3. SciKit service
4. Web Interface via Django

### Zemberek Service

Zemberek provides the NLP functionalities for the framework. The communication between the framework and Zemberek is achieved through gRPC. 

To run Zemberek service, you can use ```run_zemberek.sh```.


### Word2Vec service

Word2Vec service provides an API to get Word2Vec representations of words. You can use ```run_word2vec.sh``` to run the service.

### SciKit service

-- TODO --

### Web Interface via Django

-- TODO -- 


