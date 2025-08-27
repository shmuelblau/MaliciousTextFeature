from pymongo import MongoClient
from pymongo.database import Database

from models.logger import get_logger

log = get_logger()


class DAL:
    def __init__(self ,connection_string , db_name ) -> None:

         myclient = MongoClient(connection_string)
         self.conn:Database = myclient[db_name]
          
        
           
    def get_collections(self) -> list:
        return self.conn.list_collection_names()
    

    def get_conn(self) -> Database:
        
        return self.conn 