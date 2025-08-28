
from models.Manager import Manager
from models.config import *

import time
from models.logger import get_logger



log = get_logger()
log.info("conected")
time.sleep(25)
log.info("finish sleap")



manager = Manager(host ,topic1 , topic2 , new_topic1 , new_topic2 )





manager.start()