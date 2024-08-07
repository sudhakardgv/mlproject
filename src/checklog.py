import logging
import os
from datetime import datetime


LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()

print('log level is befor  =', LOGLEVEL)
logging.basicConfig(level=LOGLEVEL)

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#log file name should be specfed wth a directory follwed by starting word logs and then the file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


#Log file Path

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
print('log level is after =', LOGLEVEL)
print('log file path =', LOG_FILE_PATH)
print('log file =', LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,)
print('END')

if __name__ == "__main__":
    logging.info("Logging has strated ds")