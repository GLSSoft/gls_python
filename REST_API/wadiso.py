import requests
import json
from adb import AlbionDataBase as Adb

#model = "http://localhost:8080/GLS_MODEL/"
model = "http://127.0.0.1:8080/GLS_MODEL/"


class Model:

  def __init__(self):
    pass

  @staticmethod
  def Analyse(Senario1: str, Scenario2: str, ranges: str):
    '''
    Load the model at the specified location as the active model
    '''
    try:
        query_fields = '{"Function": "Analyse|' + Senario1 + '|' + Scenario2 + '","Action":"' + ranges +  '"}'
        response = requests.get(model,params=query_fields)
        data = json.loads(response.text)
        resultsDelta = {}
        for line in data:
            resultsDelta[line] = data[line]                    
        return resultsDelta   
    except:
        print("Error: filename")
        return 0

  @staticmethod
  def LoadModel(filename: str):
    '''
    Load the model at the specified location as the active model
    '''
    try:
        query_fields = '{"Function": "LoadModel","Action":"' + str(filename) +  '"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: filename")
        return 0

  @staticmethod
  def CloseModel():
    '''
    Close the current active model
    '''
    try:
        query_fields = '{"Function": "CloseModel"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: CloseModel")
        return 0

  @staticmethod
  def SwitchActiveModel():
    '''
    Launch the model display control UI
    '''
    try:
        query_fields = '{"Function": "SwitchActiveModel"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: SwitchActiveModel")
        return 0
    
  @staticmethod
  def ModelName():
    '''
    Returns the active model's name
    '''
    try:
        query_fields = '{"Function": "ModelName"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: ModelName")
        return 0
    
  @staticmethod
  def ModelPath():
    '''
    Returns the active models connection string
    '''
    try:
        query_fields = '{"Function": "ModelPath"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: ModelPath")
        return 0

  @staticmethod
  def AllTables() -> list:
    try:
        allTables = []
        query_fields = '{"Function": "AllTables"}'
        response = requests.get(model,params=query_fields)
        for str in json.loads(response.text):
            allTables.append(Adb(json.loads(response.text)[str]))
        return allTables
    except:
        print("Error: AllTables")
        return 0

  @staticmethod
  def BeginModelEvent():
    '''
    Begin recording events on the active model, required to undo changes.
    NB call EndModelEvent after using this function
    '''
    try:
        query_fields = '{"Function": "BeginModelEvent"}'
        response = requests.get(model,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: BeginModelEvent")
        return 0

  @staticmethod
  def EndModelEvent():
    '''
    End recording events on the active model, required to undo changes
    NB this must be called after using BeginModelEvent
    '''    
    try:
        query_fields = '{"Function": "EndModelEvent"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: EndModelEvent")
        return 0

  @staticmethod
  def NodeTable() -> Adb:
    try:
        query_fields = '{"Function": "NodeTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: NodeTable")
        return 0

  @staticmethod
  def SourceTable() -> Adb:
    try:
        query_fields = '{"Function": "SourceTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: SourceTable")
        return 0

  @staticmethod
  def ValveTable() -> Adb:
    try:
        query_fields = '{"Function": "ValveTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: ValveTable")
        return 0

  @staticmethod
  def PipeTable() -> Adb:
    try:
        query_fields = '{"Function": "PipeTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: PipeTable")
        return 0

  @staticmethod
  def PumpTable() -> Adb:
    try:
        query_fields = '{"Function": "PumpTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: PumpTable")
        return 0
    
  @staticmethod
  def AppurtenanceTable() -> Adb:
    try:
        query_fields = '{"Function": "AppurtenanceTable"}'
        response = requests.get(model,params=query_fields)
        return Adb(json.loads(response.text)['Result'])
    except:
        print("Error: AppurtenanceTable")
        return 0

