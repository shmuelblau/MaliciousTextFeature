

from models.kafka_loader import KafkaLoader
from models.kafka_reader import KafkaReader
from models.enricher import Enricher

from models.logger import get_logger
log = get_logger()

class Manager:

    def __init__(self , host , topic1 , topic2 , newtopic1 , newtopic2) -> None:
        self.kafka_producer:KafkaLoader = KafkaLoader(host)
        self.consumer = KafkaReader(host , topic1 ,topic2).consumer
        self.topic1 = topic1
        self.topic2 = topic2
        self.newtopic1 = newtopic1
        self.newtopic2 = newtopic2

        self.weapons = self.get_weapons()

   


    def start(self):

       

        while True:
            for line in self.consumer:
                
                newtopic = self.newtopic1 if line.topic == self.topic1 else self.newtopic2
                line = line.value
                try:
                    line = Enricher.do_all(line , self.weapons)
                    log.info("add new data")
                except Exception as e:
                    log.info(type(line))
                    log.error(e)
                

                self.kafka_producer.insert_one(newtopic,line)

        
    def get_weapons(self):
        with open('/app/models/weapons.txt' , 'r') as f:
            result = f.readlines()
            
        return result


        

    






    

