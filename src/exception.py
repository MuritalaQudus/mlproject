import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    '''
    Constructs a detailed error message including:
The script name where the error occurred.
The line number of the error.
The actual error message or exception.
    
    '''

    return error_message

    

class CustomException(Exception):# This defines CustomExceptionclass inheriting from the python built Exception Class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail) 
        '''
        Calls the error_message_detail function to generate a full, descriptive error message 
        and assigns it to self.error_message.
        
        '''
    
    def __str__(self):
        return self.error_message
    ''''
    Overrides the __str__() method so when the exception is printed or logged, 
    it returns the full detailed error message
    
    '''
    

'''
This code defines a custom exception class (CustomException) that generates detailed error messages, 
including the script name, line number, and actual error message, using traceback information. This is 
very useful in production environments for debugging and logging purposes. It enhances error transparency and
 helps developers quickly locate and understand issues in the code.


'''

        