

from kafka import KafkaConsumer
import json

class KafkaReader:

    def __init__(self ,kafka_host,  topic1 , topic2) -> None:
        self.consumer = KafkaConsumer(
            topic1 , topic2,
            bootstrap_servers=f'{kafka_host}:9092',
            auto_offset_reset='earliest',
            group_id = "Persistet",
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                       
        )
        
    
