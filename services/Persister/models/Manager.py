
from models.kafka_reader import KafkaReader
from models.DAL import DAL
from models.db_loader import DbLoader
from kafka import KafkaConsumer
from pymongo.database import Database
from models.logger import get_logger
import time
import json
log = get_logger()
class Manager:

    def __init__(self , host , topic1 , topic2 ,connection_string , dbname  ) -> None:
        try:
            log.info("try get  a consumer")
            self.consumer:KafkaConsumer = KafkaReader(host , topic1 ,topic2).consumer
            log.info("get a consumer")
        except Exception as e:
            log.error("not get consumer")
            log.error(e)
        

        self.topic1 = topic1
        self.topic2 = topic2
        self.my_connection = DAL(connection_string , dbname)
        


    def start(self):
       for line in self.consumer:
           
           self.my_connection.insert(line.topic , line.value)
        
            

    