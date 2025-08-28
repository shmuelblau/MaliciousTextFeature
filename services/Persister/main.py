
from models.Manager import Manager
from models.config import *
import asyncio
import time
from models.logger import get_logger



log = get_logger()
log.info("conected")
time.sleep(25)
log.info("finish sleap")


try:
    manager = Manager(host ,topic1 , topic2 ,connection_string , dbname )
    log.info("create a manager")
except Exception as e:
    log.error("not manager")



try:
    log.info("start to work")
    manager.start()
    
except Exception as e:
    log.error("not start")


