import os 

host = os.getenv("HOST" , "kafka")
connection_string = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/TextFeature?authSource=admin")

dbname = os.getenv("DB_NAME" ,"TextFeature" )

topic1 = os.getenv("NEW_TOPIC1" ,"enriched_preprocessed_tweets_antisemitic")     
topic2 = os.getenv("NEW_TOPIC2" ,"enriched_preprocessed_tweets_not_antisemitic")    


