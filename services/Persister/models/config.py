import os 

host = os.getenv("HOST" , "kafka")
connection_string = os.getenv("CONNECTION_STRING" ,"mongodb://shmuel:1234@mongo:27017/iran?authSource=admin")