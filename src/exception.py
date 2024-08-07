import sys
from logger import logging


def error_messages(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #not interested in the forst 2 return values but 3rd has all the details on error
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message= "Error Occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    #This class inherits from the excpetion class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

         #class var is getting assigned with the error message received
        self.error_message=error_messages(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


'''
commented to test the code
if __name__=="__main__":
    try:
        a= 1/0
           
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
'''

    

