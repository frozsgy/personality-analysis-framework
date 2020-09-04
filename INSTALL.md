# Installation Manual for the Personality Analysis Framework

## Creating config.yml 

Use ```setup.py``` to generate the configuration file, ```config.yml```. After training the Word2Vec model, you need to run ```config_boundaries.sh``` to generate boundary values for the normalization process. This updates the ```config.yml``` with accordance to these values and it is crucial for the following steps.

## Training Phase

### Training Word2Vec Model

In order to get Word2Vec representations properly, you need to train the Word2Vec library using ```train_model.sh```. This step uses the Wikipedia archive for Turkish language to create a vector space to represent words.

### Acquiring Ground Truths

You need to acquire OCEAN scores for your ground truth users. You may do it with a questionnaire, or other methods. We do not provide a concrete code block for this step, since it may vary vastly.

You also need to create the vector representation of your ground truth users. While determining the best pipeline via TPOT, you will need 5 different ground truth vectors with the following structure:
``` 
OCEAN_SCORE,d0,d1,d2,....,dn
```

The OCEAN_SCORE refers to the trait that the vector belongs to, and the rest is the values of the dimensions.

Place your ground truth vectors in the ```predictors/tpot``` folder with the following naming style: ```resultvector-{dimensions}-{top_words}-{window_size}-{trait}.csv``` where dimensions refers to the Word2Vec dimensions, top_words refers to the TFxIDF top word count, window_size refers to Word2Vec window size, and trait refers to the OCEAN trait.

### Training Machine Learning Model

After acquiring the ground truth vectors, you need to train your machine learning model to use with the system. In order to achieve the optimal training, we use TPOT. TPOT determines the optimal pipeline for each personality trait and reports the pipeline, which you should implement in your system.

Run TPOT via the ```teapot.py``` file inside the ```predictors/tpot``` folder. It should take a while depending on your system to determine the best prediction algorithm. For each personality trait, you must copy the pipeline and paste it inside the ```main.py``` to allow the system to predict personality types.

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


