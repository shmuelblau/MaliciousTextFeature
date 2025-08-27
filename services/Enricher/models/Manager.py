

from models.kafka_loader import KafkaLoader
from models.kafka_reader import KafkaReader

class Manager:

    def __init__(self , host , topic1 , topic2 , newtopic1 , newtopic2) -> None:
        self.kafka_producer:KafkaLoader = KafkaLoader(host)
        self.consumer = KafkaReader(host , topic1 ,topic2).consumer
        self.topic1 = topic1
        self.topic2 = topic2
        self.newtopic1 = newtopic1
        self.newtopic2 = newtopic2

   


    def start(self):

       

        while True:
            for line in self.consumer:
                
              
                # line = Enricher.do_all(line)
                newtopic = self.newtopic1 if line.topic == self.topic1 else self.newtopic2
                line = line.value
                self.kafka_producer.insert_one(newtopic,line)

        

            


        

    






    

