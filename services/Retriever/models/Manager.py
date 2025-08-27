
from models.DAL import DAL
from models.db_loader import DbLoader
from models.logger import get_logger
from models.kafka_loader import KafkaLoader
from models.funcs import *

log = get_logger()

class Manager:
# --------------------------------------------------------------------------------------

    def __init__(self , connection_string ,dbname ,collection , kafka_host ) -> None:

        try:
            dal:DAL = DAL(connection_string , dbname)
            self.dbloader = DbLoader(dal , collection)
            self.kafkaloader = KafkaLoader(kafka_host)
            self.start = 0
        except Exception as e:
            log.info("can't create db loader")
            log.info(e)

# --------------------------------------------------------------------------------------
    def pull_and_push(self):
        try:
            data = self.get_Messages()
            log.info("start filter")

            raw_tweets_antisemitic:list = filter_by_info(data , 'Antisemitic' , 1 )
            raw_tweets_not_antisemitic = filter_by_info(data , 'Antisemitic' , 0 )

            self.kafkaloader.insert("raw_tweets_antisemitic" , raw_tweets_antisemitic)
            self.kafkaloader.insert("raw_tweets_not_antisemitic" , raw_tweets_not_antisemitic)
        except Exception as e:
            log.info("field pull_and_push ")
            log.info(e)


        

# --------------------------------------------------------------------------------------

    def get_Messages(self  ,limit = 100) -> list[dict]:
            
        try:
            aggregat = get_aggregat(self.start , limit)

            self.start += 100

            data = self.dbloader.Aggregat(aggregat)
            log.info(f"success get a data len:{len(data)}")

        except Exception as e:
            log.info(f'error:{e}')

        return data
        

# --------------------------------------------------------------------------------------

    

# --------------------------------------------------------------------------------------




    
        


        

    






    

