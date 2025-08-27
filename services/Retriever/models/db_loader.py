import pymongo
from models.DAL import DAL
from pymongo.database import Database ,Collection
from models.logger import get_logger

log = get_logger()

class DbLoader:
    
    def __init__(self,db_connection:DAL  , collection_name):
        
        self.connection:Database = db_connection.get_conn()
        self.collection_name = collection_name
        
        self.collection:Collection = self.connection[collection_name]
        
        

   
# ---------------------------------------------------------------------------------------

    def Aggregat(self , aggregat:list ) -> list[dict] :

        try:
            data = list(self.collection.aggregate(aggregat))
            log.info(f"select a data len ={len(data)}")
            for line in data:
                line["CreateDate"] = str(line["CreateDate"])
            
        except Exception as e:
            log.info("select failed")
            log.info(f"type error {e}")

        return data
        
        
# ---------------------------------------------------------------------------------------
    def insert(self , data:list[dict]) -> None:

        for d in data:
            d.pop("_id", None)
        log.info(f"start load data len ={len(data)}")

        try:
            self.connection[self.collection_name].insert_many(data)
            log.info("load finish")

        except Exception as e:
            log.info("insert failed")
            log.info(f"type error {e}")
        

               

    