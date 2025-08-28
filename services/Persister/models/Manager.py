
from models.kafka_reader import KafkaReader
from models.DAL import DAL
from models.db_loader import DbLoader

from pymongo.database import Database
class Manager:

    def __init__(self , host , topic1 , topic2 ,connection_string , dbname  ) -> None:

        self.consumer = KafkaReader(host , topic1 ,topic2).consumer
        self.topic1 = topic1
        self.topic2 = topic2
        self.my_connection = DAL(connection_string , dbname)
       
        self.sdloaders = {topic1: DbLoader(self.my_connection , topic1) , topic2:DbLoader(self.my_connection , topic2)}


    






    

