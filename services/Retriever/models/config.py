import os 


dbname = os.getenv("DATABASE" , "IranMalDB")
collection = os.getenv('COLLECTION',"tweets")
connection_string = os.getenv("CONNECTION_STRING" ,"mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")

host = os.getenv("HOST" , "localhost")
topic1 = os.getenv("TOPIC1" ,"raw_tweets_antisemitic")     
topic2 = os.getenv("TOPIC2" ,"raw_tweets_not_antisemitic")         
