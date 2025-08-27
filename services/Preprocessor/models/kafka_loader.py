from kafka import KafkaProducer
from models.logger import get_logger

log = get_logger()
class KafkaLoader:

    def __init__(self , host) -> None:
        self.producer = KafkaProducer(
                        bootstrap_servers = f'{host}:9092',
                        value_serializer=lambda v: v.encode('utf-8')
                    )
        

    
    def insert_meny(self ,topic , data:list):
        try:
            log.info(f"try insert data topic:{topic}  len:{len(data)}")
            for i in data:
                i = str(i)
                self.producer.send(topic , i )

            self.producer.flush()
            log.info("success insert")

        except Exception as e:
            log.info("failed insert data to kafka")
            log.info(f"error:{e}")

    def insert_one(self ,topic , data:dict):
        try:
            i = str(data)
            self.producer.send(topic , i )

            self.producer.flush()
            log.info("success insert")

        except Exception as e:
            log.info("failed insert data to kafka")
            log.info(f"error:{e}")

