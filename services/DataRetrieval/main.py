from fastapi import FastAPI
 
import uvicorn
from models.config import *
from models.Manager import Manager




from models.logger import get_logger



app = FastAPI()

log =  get_logger()

manager = Manager(connection_string , dbname , collection1 ,collection2)



log.info(f"dbname ={dbname}")




# =================================================================



@app.get("/antisemitic")
def antisemitic():

    data = manager.get(collection1)
    log.info(F"return a data len {len(data)}")
    
    return list(data)

@app.get("/not_antisemitic")
def not_antisemitic():

    data = manager.get(collection2)
    log.info(F"return a data len {len(data)}")
    
    return list(data)
if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)