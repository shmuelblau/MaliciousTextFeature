from models.Manager import Manager
from models.config import *

import time

manager = Manager(connection_string , dbname, collection , host )


for i in range(10):
    time.sleep(10)
    manager.pull_and_push()

