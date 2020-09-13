import yaml
from web.db import DB
from mysql.connector import connect
import os

print("This tool will create the yaml file to store configuration details.")

print("\nGeneral Details")
url = input("URL of your website(with http or https prefix): ")

print("\nDatabase Details")
db_host = input("Database host: ")
db_user = input("Database username: ")
db_pass = input("Database password: ")
db_name = input("Database name: ")
try:
    connect(user=db_user, password=db_pass, host=db_host, database=db_name, autocommit=True)
    print("Database connection succesful")
except:
    print("Can't connect to database, check credentials")
    exit()


print("\nTwitter API Details")
consumer_key = input("Consumer key: ")
consumer_secret = input("Consumer secret: ")
callback_url = input("Callback URL: ")

print("\nWord2Vec Service Details")
word2vec_check = input("Will you run Word2Vec service on another machine? y/n ")
if word2vec_check == "y":
    word2vec_url = input("Type the URL of the machine with http or https: ")
else:
    word2vec_url = "http://127.0.0.1"
word2vec_port_check = input(
    "Word2Vec service uses port 5000 as default. Do you want to change it? y/n ")
if word2vec_port_check == "y":
    word2vec_port = input("Enter port: ")
    try:
        word2vec_port = int(word2vec_port)
    except:
        word2vec_port = 5000
        print("Invalid port, using 5000 as default")
else:
    word2vec_port = 5000

print("\nWord2Vec Details")
try:
    word2vec_max_features = int(input(
        "Enter number of top words for TFxIDF: "))
except:
    print("Invalid top word count, using 25 as default")
    word2vec_max_features = 25
try:
    word2vec_dimension = int(input(
        "Enter number of dimensions for the Word2Vec embedding: "))
except:
    print("Invalid dimension, using 100 as default")
    word2vec_dimension = 100
try:
    word2vec_window = int(input("Enter number of windows for Word2Vec embedding: "))
except:
    print("Invalid windows, using 7 as default")
    word2vec_window = 7
try:
    word2vec_min_count = int(input(
        "Enter minimum number of counts for Word2Vec embedding: "))
except:
    print("Invalid minimum count, using 3 as default")
    word2vec_min_count = 3

pwd = os.getcwd()

config = {"twitter": {"consumer_key": consumer_key,
                      "consumer_secret": consumer_secret,
                      "callback_url": callback_url},
          "word2vec": {
    "service": {
        "url": word2vec_url,
        "port": word2vec_port},
    "vector": {
        "max_features": word2vec_max_features,
        "dimension": word2vec_dimension,
        "window": word2vec_window,
        "min_count": word2vec_min_count}},
    "pwd": pwd,
    "url": url,
    "database": {
        "user": db_user,
        "password": db_pass,
        "host": db_host,
        "database": db_name
    }
}

with open("config.yml", "w") as file:
    yaml.dump(config, file)

print("Configuration file created successfully")


print("Creating database tables...")
db = DB(config)
db.create_db()

print("Tables created successfully")

