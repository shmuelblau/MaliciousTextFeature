import os 



dbname = os.getenv("DATABASE" , "TextFeature")
collection1 = os.getenv('COLLECTION1',"enriched_preprocessed_tweets_antisemitic")
collection2 = os.getenv('COLLECTION2',"enriched_preprocessed_tweets_not_antisemitic")

connection_string = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/TextFeature?authSource=admin")

