import os
import sys
sys.dont_write_bytecode = True
sys.path.append(os.getcwd()) # To add current working directory to the path. This includes mlproject\src\components
sys.path.insert(0, 'C:\\Varshini\\SudhakarD\\PandasFiles\\ML\\mlproject\\src') #when inspected using sys.path the path C:\\Varshini\\SudhakarD\\PandasFiles\\ML\\mlproject\\src
#print(sys.path) was not there so added to the sys
#exit()
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import Data_Transformation
from src.components.data_transformation import Data_Transformation_Config
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

@dataclass
class DataIngestionConfig:
    #print('os path=', os.path)
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"rawdata.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered data ingestion')
        try:
            df=pd.read_csv('C:\\Varshini\\SudhakarD\\PandasFiles\\ML\\mlproject\\data\\stud.csv')
            logging.info('Data is read into dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #Saving raw data to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Raw Data is savedto artifact')
            logging.info('Train test split has started')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion is complete')

            return(
                self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            ) 
        except Exception as e:
            raise CustomException (e,sys)

# To test the code
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=Data_Transformation()
    train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    





    