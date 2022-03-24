from REST_GLS_Interface import GLS_REST_INTERFACE as GLS_Interface
from REST_GLS_Interface import bcolors as bcolors
from flask import appcontext_popped
from matplotlib.font_manager import json_load
from shapely.geometry.base import BaseGeometry
from shapely import wkt
from shapely.geometry import Point, LineString, Polygon
from enum import IntEnum
import requests
import json
import geopandas as gpd
import inspect

adb = "http://127.0.0.1:8080/GLS_ADB/"

class AlbionFieldTypes(IntEnum):
    AdbFTNull                   = 0
    AdbFTBool                   = 1
    AdbFTInt32                  = 2
    AdbFTInt64                  = 3
    AdbFTDouble                 = 4
    AdbFTText                   = 5
    AdbFTDate                   = 6
    AdbFTGuid                   = 7
    AdbFTTime                   = 8
    AdbFTBin                    = 9
    AdbFTGeomBEGIN              = 32
    AdbFTGeomPoint              = AdbFTGeomBEGIN
    AdbFTGeomMultiPoint         = 33
    AdbFTGeomPolyline           = 34
    AdbFTGeomPolygon            = 35
    AdbFTGeomEND                = 36   

class AlbionDataBase:        
    def __init__(self,iTable=-1):
        self.FTable = -1
        if iTable != -1:
            self.session = requests.Session()
            self.FTable = iTable

    #def CreateTable(self,iName):
    #    self.FTable = adb.CreateTable(iName)

    def Pointer(self):
        return self.FTable
        
    def GetSetMethod(self,iFunc,iFld=-1,iRec=-1,iValue=-1,iRecords=[],iValues=[],iAction=-1,iRaw=False):
        try:
            query_fields = {
                "Function":iFunc,
                "Table":str(self.FTable),
                "Field":str(iFld),
                "Record":str(iRec),
                'Value':str(iValue),
                "Action":iAction,
                "Records":[],
                'Values':[]
                }
                
            for i in iRecords:
                query_fields['Records'].append(i)
                
            for i in iValues:
                query_fields['Values'].append(i)
            
            return GLS_Interface.AlbionPOST(adb,query_fields,iRaw)      
        except:
            bcolors.print_fail("Error: " + iFunc)
            return 0     
        
    def Info(self):
        bcolors.print_header(self.Name())
        bcolors.print_normal("Field Count: " + str(self.FieldCount()))
        bcolors.print_normal("Record Count: " + str(self.RecordCount()))
        
        #for i in range(self.FieldCount()):
        #    self.FieldInfo(i)    
        
    def FieldInfo(self,fld):
        bcolors.print_underline("Name: " + self.FieldName(fld))  
        bcolors.print_normal("Type: " + str(self.FieldType(fld)))
        
    
    def Name(self):
        """
        Returns the table name of the current object     
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name) 
        
    def FieldIndex(self,iName): 
        """
        Returns the index of the field name. A -1 result means the field does not exist      
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iName) 

    def RecordCount(self): 
        """
        Returns the number of records in the table.
        Remember to use IsRecordAlive to ensure a record has not been deleted.
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name)          

    def GetDouble(self,iFld,iRec): 
        """
        Returns the index of the field name. A -1 result means the field does not exist      
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec) 
        
    def FieldIndexGeom(self): 
        """
        Returns the index of the first geometry field. A -1 result means the field does not exist      
        """
        return self.FieldIndex("Geometry")
    
    def FieldName(self,iFld):  
        """
        Returns the name of the field at the current index. An invalid number will cause an error
        Use fieldindex to get a proper index      
        """       
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld) 
        
    def FieldCount(self): 
        """
        Returns the number of fields in the table      
        """        
        return self.GetSetMethod(inspect.currentframe().f_code.co_name) 

    def FieldType(self,iFld): 
        """
        Returns a string represenation of the field type    
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld) 
        
    def IsRecordAlive(self,iRec): 
        """
        Returns a bool value where false implies the record does not exist anymore     
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iRec=iRec) 
        
    def GetText(self,iFld,iRec): 
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec) 
        
    def GetInteger(self,iFld,iRec):   
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec) 

    def GetBool(self,iFld,iRec):  
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec) 

    def GetPolygon(self,iFld,iRec) -> Polygon: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iRaw=True)  
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            bcolors.print_fail("Error: GetPolygon")
            return 0 
        
    def GetPolyline(self,iFld,iRec) -> LineString:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry        
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iRaw=True) 
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            bcolors.print_fail("Error: GetPolyline")
            return 0
        
    def GetPoint(self,iFld,iRec) -> Point: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iRaw=True) 
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            bcolors.print_fail("Error: GetPoint")
            return 0
        
    def GetPointAll(self) -> list:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iRaw=True)   
            data = json.loads(response.text)
            wktArray = []
            for line in data:
                wktArray.append(data[line])           
            allGeom = gpd.GeoSeries.from_wkt(wktArray)                                                       
            return allGeom
        except:
            bcolors.print_fail("Error: GetPointAll")
            return 0
        
    def GetPolylineAll(self) -> list:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iRaw=True)  
            data = json.loads(response.text)
            wktArray = []
            for line in data:
                wktArray.append(data[line])           
            allGeom = gpd.GeoSeries.from_wkt(wktArray)                                                       
            return allGeom
        except:
            bcolors.print_fail("Error: GetPolylineAll")
            return 0
        
    def GetPolygonAll(self) -> list:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iRaw=True)  
            allGeom = []
            data = json.loads(response.text)
            for line in data:
                allGeom.append(wkt.loads(data[line]))            
            return allGeom
        except:
            bcolors.print_fail("Error: GetPolygonAll")
            return 0  

    def GetDoubleAll(self,iFld) -> list: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld=iFld,iRaw=True) 
            data = json.loads(response.text)
            result = []
            for line in data:
                result.append(data[line])      
            return  result
        except:
            bcolors.print_fail("Error: GetDoubleAll")
            return 0

    def GetIntegerAll(self,iFld) -> list: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld=iFld,iRaw=True) 
            data = json.loads(response.text)
            result = []
            for line in data:
                result.append(data[line])      
            return  result
        except:
            bcolors.print_fail("Error: GetIntegerAll")
            return 0

    def GetBoolAll(self,iFld) -> list: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld=iFld,iRaw=True) 
            data = json.loads(response.text)
            result = []
            for line in data:
                result.append(data[line])      
            return  result
        except:
            bcolors.print_fail("Error: GetBoolAll")
            return 0

    def GetTextAll(self,iFld) -> list: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            response = self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld=iFld,iRaw=True) 
            data = json.loads(response.text)
            result = []
            for line in data:
                result.append(data[line])      
            return  result
        except:
            bcolors.print_fail("Error: GetTextAll")
            return 0            
              
    def GetValuesFromRecordArray(self,iFld,recordArray) -> list:  
        try:            
            list = ''
            for i in recordArray:
                list = list + str(i) + ';'
            
            query_fields = {
                "Function":"GetValuesFromRecordArray",
                "Table": str(self.FTable),
                "Field": str(iFld),
                "Records": list
                }
            
                
            response = self.AlbionPOST(query_fields,True)   
            all = []
            data = json.loads(response.text)
            for line in data:
                all.append(data[line])            
            return all
        except:
            bcolors.print_fail("Error: GetPolygonAll")
            return 0
        
    def SetDouble(self,iFld,iRec,iValue):
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iValue)  
    
    def SetInteger(self,iFld,iRec,iValue):
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iValue)     
       
    def SetText(self,iFld,iRec,iValue):
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iValue) 
       
    def SetBool(self,iFld,iRec,iValue):
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRec,iValue)         

    def SetPoint(self,iFld,iRec,iValue): 
        return self.GetSetMethod(self.FTable,iFld,iRec,str(iValue))

    def SetPolyline(self,iFld,iRec,iValue: LineString):  
        return self.GetSetMethod(self.FTable,iFld,iRec,str(iValue))

    def SetPolygon(self,iFld,iRec,iValue): 
        return self.GetSetMethod(self.FTable,iFld,iRec,str(iValue))
        
    def SetDoubleArray(self,iFld,iValues):            
        records = []
        for i in iValues:
            records.append(i)
            
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld,iRecords=records) 
        
    def SetIntegerArray(self,iFld,iValues):
        try:
            query_fields = {
                    'Function': 'SetIntegerArray',
                    'Table': str(self.FTable),
                    'Field': str(iFld),
                    'Records':[]
                }

            for i in iValues:
                query_fields['Records'].append(i)
                
            return self.AlbionPOST(query_fields,False)   
        except:
            bcolors.print_fail("Error: SetIntegerArray")
            return 0
        
    def SetBoolArray(self,iFld,iValues):
        try:
            query_fields = {
                    'Function': 'SetBoolArray',
                    'Table': str(self.FTable),
                    'Field': str(iFld),
                    'Records':[]
                }

            for i in iValues:
                query_fields['Records'].append(i)
                
            return self.AlbionPOST(query_fields,False)   
        except:
            bcolors.print_fail("Error: SetBoolArray")
            return 0
        
    def SetTextArray(self,iFld,iValues):
        try:
            query_fields = {
                    'Function': 'SetTextArray',
                    'Table': str(self.FTable),
                    'Field': str(iFld),
                    'Records':[]
                }

            for i in iValues:
                query_fields['Records'].append(i)
                
            return self.AlbionPOST(query_fields,False)   
        except:
            bcolors.print_fail("Error: SetTextArray")
            return 0
        
    def Lock(self):
        return self.GetSetMethod(inspect.currentframe().f_code.co_name) 
    
    def EraseRecord(self,iRec): 
        """
        Erases a single record in the table     
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iRec=iRec) 
    
    def EraseAllRecords(self): 
        """
        Erases all records in the table     
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name) 
    
    def EraseField(self,iFld): 
        """
        Erases a single field from the table    
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name,iFld) 
    
    def Flush(self): 
        """
        Saves the database    
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name) 
    
    def AddRecord(self): 
        """
        Adds a record and returns the new record index  
        """
        return self.GetSetMethod(inspect.currentframe().f_code.co_name)     
    
'''
    def AddField(self,iName: str,iType: AlbionFieldTypes):
        """
            AdbFTNull                   = 0;
            AdbFTBool                   = 1;
            AdbFTInt32                  = 2;
            AdbFTInt64                  = 3;
            AdbFTDouble                 = 4;
            AdbFTText                   = 5;
            AdbFTDate                   = 6;
            AdbFTGuid                   = 7;
            AdbFTTime                   = 8;
            AdbFTBin                    = 9;
            AdbFTGeomBEGIN              = 32;
            AdbFTGeomPoint              = AdbFTGeomBEGIN;
            AdbFTGeomMultiPoint         = 33;
            AdbFTGeomPolyline           = 34;
            AdbFTGeomPolygon            = 35;
            AdbFTGeomEND                = 36;
        """
        print(str(iType))
        return adb.AddField(self.FTable,iName,iType)


    def RecordsFromValue(self,iFld: int,iValue: str) -> list:
        result = []
        values = adb.RecordsFromValue(self.FTable,iFld,iValue)
        if not values is None:
            for value in values:
                result.append(value)
        return result

    def WhereClause(self,iQuery: str) -> list:
        """
        Insert the part of the where clause after WHERE. The query will only run on this table
        """
        result = []
        values = adb.SqlWhereClause(self.FTable,iQuery)
        if not values is None:
            for value in values:
                result.append(value)
        return result

    def RecordsContainingTextValue(self,iFld: str,iValue: str) -> list:
        result = []
        values = adb.RecordsContainingTextValue(self.FTable,iFld,iValue)
        if not values is None:
            for value in values:
                result.append(value)
        return result

    def GetDistinctTextValues(self,iFld: int) -> list:
        result = []
        values = adb.GetDistinctTextValues(self.FTable,iFld)
        if not values is None:
            for value in values:
                result.append(value)
        return result

    def GetDistinctTextValuesNaturalSort(self,iFld: int) -> list:
        result = []
        values = adb.GetDistinctTextValuesNaturalSort(self.FTable,iFld)
        if not values is None:
            for value in values:
                result.append(value)
        return result
'''