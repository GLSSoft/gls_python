from itsdangerous import JSONWebSignatureSerializer
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from abgis import AlbionGisLayer as AbGIS

#url = "http://localhost:8080/Active"
#response = requests.get(url)
#print(response.text)

#convert data to pands data frame    
url = "http://localhost:8080/GLS/"
try:    
    #query_fields = {"MODEL": "OpenAndReplaceModelFromString|C:\\Users\\adrian\\Documents\\GLS\\Wadiso\\Wadiso 6 - Tutorial TS_backup.wlz"}
    #response = requests.get(url,params=query_fields)    
    
    #query_fields = {"MODEL": "HydraulicChecks"}
    #response = requests.get(url,params=query_fields)   
    
    query_fields = {"MODEL": "BalanceModel"}
    response = requests.get(url,params=query_fields)   
    
    requests.post() 
    
    query_fields = {"MODEL": "Name"}
    response = requests.get(url,params=query_fields)
    print(json.loads(response.text))
    
    query_fields = {"PIPEDATA": "3"}
    response = requests.get(url,params=query_fields)
    a_json = json.loads(response.text)
    dFrame = pd.DataFrame.from_dict(a_json, orient="index")
    print(dFrame)
    
    query_fields = {"PIPEDATA": "Flow"}
    response = requests.get(url,params=query_fields)
    a_json = json.loads(response.text)
    dFrame = pd.DataFrame.from_dict(a_json, orient="index")    
    print(dFrame)  
      
    query_fields = {"PIPEDATA": "ALL"}
    response = requests.get(url,params=query_fields)
    a_json = json.loads(response.text)
    dFrame = pd.DataFrame.from_dict(a_json, orient="index")
    for str in list(dFrame.columns):
        print(str)
        
    dFrame.plot(kind="scatter",x="Diameter",y="Flow",color="red")
    plt.show()

except:
    print("Error")
    
    