

from kafka import KafkaConsumer


class KafkaReader:

    def __init__(self ,kafka_host,  topic1 , topic2) -> None:
        self.consumer = KafkaConsumer(
            topic1 , topic2,
            bootstrap_servers=f'{kafka_host}:9092',
            auto_offset_reset='earliest',
            group_id = "preprosesor",
            value_deserializer=lambda v: v.decode('utf-8'),
                       
        )
        
    
