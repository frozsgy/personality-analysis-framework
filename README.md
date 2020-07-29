# personality-analysis-framework





## Data Collection

With dl_tweets.py

## Data Preprocess

1. Preprocess

with preprocess.py

2. Normalization

3. Lemmatization

## Vector Construction

1. Feature Extraction

2. Feature Reduction

3. Normalization

4. TF-IDF Weighting and Word2Vec based Word Embedding

5. Composition of Extracted Features and Word2Vec Vectors

## Clustering



## Usage
0. Train the Word2Vec library using ```./train_model.sh```. This step should be done only for the initial run.
1. Run Zemberek as a service ```./run_zemberek.sh``` 
2. Run Word2Vec service via ```./run_word2vec.sh```
3. Run the Python script either with ```python main.py username``` for giving username as an argument, or ```python main.py``` for entering username when asked
4. ```python main.py username --debug``` downloads only the recent 200 tweets to allow faster debugging.


## Reading from a CSV file

It is possible to download tweets of a user and use this csv file for the vector construction. In order to do so, do the following steps:
1. Download tweets of a user via ```python download-tweets.py```. This will save the tweets in the ```data/tweets``` folder.
2. Run the vector constructor via ```python main.py username --file``` arguments. This will read the tweets from the csv file instead of downloading them from scratch. 

This method was implemented to avoid burning out the Twitter API for recurrent downloads.