import pandas as pd
import sys,os
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
sys.dont_write_bytecode = True
sys.path.append(os.getcwd()) # To add current working directory to the path. This includes mlproject\src\components
sys.path.insert(0, 'C:\\Varshini\\SudhakarD\\PandasFiles\\ML\\mlproject\\src') #when inspected using sys.path the

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
@dataclass 
class Data_Transformation_Config:
    preprocessor_file_path=os.path.join('artifacts','preprocessor.pkl')

class Data_Transformation:
    def __init__(self):
        self.data_transformation_config = Data_Transformation_Config()
    
    def get_transformation_object(self):
        '''
        This fn is responsible for data transformation 
        '''
        try:
            numcols=['writing_score','reading_score']
            catcols=['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']

            num_pipeline= Pipeline(steps=[("imputer",SimpleImputer(strategy='median')),("scaler",StandardScaler())])
            cat_pipeline= Pipeline(steps=[("imputer", SimpleImputer(strategy='most_frequent')),
                                            ("one_hot_encoder",OneHotEncoder()),
                                            ("scaler", StandardScaler(with_mean=False))
                                            ]
                                    )
            
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )
            logging.info(f'Numerical columns: {numcols}')
            logging.info(f'Categgorical columns: {catcols}')

            preprocessor =ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numcols),
                    ('cat_pipeline',cat_pipeline,catcols)
                ]
            )

            logging.info('Numerical columns standard scaling completed')
            logging.info('Categgorical columns standard scaling completed')
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            
            train_df = pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('Read train and test data completed')
            logging.info('Reading preproceccor object')
            preprocessing_obj = self.get_transformation_object()
            target_column_name="math_score"
            target_column = 'math_score'
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path,
            )
        except Exception as e:
            raise CustomException (e,sys)
