import logging
import logger
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#log file name should be specfed wth a directory follwed by starting word logs and then the file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


#Log file Path

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

'''
commented to test the code

if __name__=="__main":
    LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
    print(LOGLEVEL)
    logging.basicConfig(level=LOGLEVEL)
    logging.setLevel(logging.INFO)
    logging.info("Logging has strated")
'''