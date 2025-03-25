import sys

def error_msg_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    error_message="error occurred in python script"