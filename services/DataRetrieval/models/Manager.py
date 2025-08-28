from models.db_loader import DbLoader

from models.logger import get_logger
from models.DAL import DAL
log = get_logger()
class Manager:
    
    def __init__(self , connection_string , db_name ,collection1 ,collection2 ) -> None:

        self.db:DAL = DAL(connection_string ,db_name )
        self.dbloader = {collection1:DbLoader(self.db  , collection1) , collection2: DbLoader(self.db  , collection2)} 
   

        
    
    def get(self , coll):

        result = self.dbloader[coll].Select()
      

        return result
    


