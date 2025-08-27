import os 

host = os.getenv("HOST" , "kafka")

topic1 = os.getenv("TOPIC1" ,"raw_tweets_antisemitic")     
topic2 = os.getenv("TOPIC2" ,"raw_tweets_not_antisemitic") 


new_topic1 = os.getenv("NEW_TOPIC1" ,"preprocessed_tweets_antisemitic")     
new_topic2 = os.getenv("NEW_TOPIC2" ,"preprocessed_tweets_not_antisemitic")    