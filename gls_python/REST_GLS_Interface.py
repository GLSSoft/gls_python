from flask import appcontext_popped
from matplotlib.font_manager import json_load
import requests
import json  

class GLS_REST_INTERFACE:        
    def __init__(self):
        pass

    @staticmethod
    def AlbionPOST(connection,query,raw_result=False):
        try:
            headers = {'Content-Type': 'application/json'}
            content = json.dumps(query)
            response = requests.request('POST',connection,headers=headers,data=content)
            if raw_result:
                return response
            else:
                return json.loads(response.text)['Result']
        except:
            bcolors.print_fail("AlbionPOST Error: " + query)
            return 0  
                

class bcolors:
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
    
    @staticmethod
    def print_fail(message):
        print('\033[91m'+message+'\033[0m')
        
    @staticmethod
    def print_green(message):
        print('\033[92m'+message+'\033[0m')
        
    @staticmethod
    def print_cyan(message):
        print('\033[96m'+message+'\033[0m')
        
    @staticmethod
    def print_blue(message):
        print('\033[94m'+message+'\033[0m')   
        
    @staticmethod
    def print_header(message):
        print('\033[95m'+message+'\033[0m')   
        
    @staticmethod
    def print_underline(message):
        print('\033[4m'+message+'\033[0m')  
        
    @staticmethod
    def print_bold(message):
        print('\033[1m'+message+'\033[0m')    
    @staticmethod
    def print_normal(message):
        print(message)   
        