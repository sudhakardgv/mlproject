import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

sys.dont_write_bytecode = True
sys.path.append(os.getcwd()) # To add current working directory to the path. This includes mlproject\src\components
sys.path.insert(0, 'C:\\Varshini\\SudhakarD\\PandasFiles\\ML\\mlproject\\src') #when inspected using sys.path the
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)