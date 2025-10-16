import sys
from networksecurity.logging import logger

class NetSecurityException(Exception):
    def __init__(self,error_message,error_details):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()

        self.lineno=exc_tb.tb_lineno if exc_tb else None
        self.file_name=exc_tb.tb_frame.f_code.co_filename if exc_tb else None
    
    def __str__ (self):
        return "Error in python project [{0}] line num [{1}] msg [{2}]", self.file_name, self.lineno, str(self.error_message)
    
