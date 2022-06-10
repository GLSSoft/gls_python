from REST_GLS_Interface import GLS_REST_INTERFACE as GLS_Interface
from REST_GLS_Interface import bcolors as bcolors
import json
from REST_adb import AlbionDataBase as Adb
import inspect

model = "http://127.0.0.1:8080/GLS_MODEL/"

class Model:

    def __init__(self):
        pass        
        
    @staticmethod
    def CallFunctionWithAction(iName,iAction=-1,raw_result=False) -> Adb:
        try:
            query_fields = {
                "Function": iName,
                "Action": iAction
                }
            return GLS_Interface.AlbionPOST(model,query_fields,raw_result) 
        except:
            bcolors.print_fail("Error: " + iName)
            return 0

    @staticmethod
    def Analyse(Senario1: str, Scenario2: str, ranges: str):
        '''
        Load the model at the specified location as the active model
        '''
        try:
            function = "Analyse|" + Senario1 + "|" + Scenario2
            action = ranges
            response = Model.CallFunctionWithAction(function,action,True)
            data = json.loads(response.text)
            resultsDelta = {}
            for line in data:
                resultsDelta[line] = data[line]                    
            return resultsDelta   
        except:
            bcolors.print_fail("Error: filename")
            return 0

    @staticmethod
    def LoadModel(filename: str):
        '''
        Load the model at the specified location as the active model
        '''
        name = inspect.currentframe().f_code.co_name
        action = filename
        return Model.CallFunctionWithAction(name,action)

    @staticmethod
    def CloseModel():
        '''
        Close the current active model
        '''
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)

    @staticmethod
    def SwitchActiveModel():
        '''
        Launch the model display control UI
        '''
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)
    
    @staticmethod
    def ModelName():
        '''
        Returns the active model's name
        '''
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)
    
    @staticmethod
    def ModelPath():
        '''
        Returns the active models connection string
        '''
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)

    @staticmethod
    def AllTables() -> list:
        response = Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name,raw_result=True)
        allTables = []
        for str in json.loads(response.text):
            allTables.append(Adb(json.loads(response.text)[str]))
        return allTables

    @staticmethod
    def BeginModelEvent():
        '''
        Begin recording events on the active model, required to undo changes.
        NB call EndModelEvent after using this function
        '''
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)

    @staticmethod
    def EndModelEvent():
        '''
        End recording events on the active model, required to undo changes
        NB this must be called after using BeginModelEvent
        '''    
        return Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name)

    @staticmethod
    def NodeTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))

    @staticmethod
    def SourceTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))

    @staticmethod
    def ValveTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))

    @staticmethod
    def PipeTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))

    @staticmethod
    def PumpTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))
    
    @staticmethod
    def AppurtenanceTable() -> Adb:
        return Adb(Model.CallFunctionWithAction(inspect.currentframe().f_code.co_name))

