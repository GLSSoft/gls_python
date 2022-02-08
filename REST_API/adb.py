from flask import appcontext_popped
from matplotlib.font_manager import json_load
from shapely.geometry.base import BaseGeometry
from shapely import wkt
from shapely.geometry import Point, LineString, Polygon
from enum import IntEnum
import requests
import json
import time
from tqdm import tqdm

#adb = "http://localhost:8080/GLS_ADB/"
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

    def Name(self):
        """
        Returns the table name of the current object     
        """
        try:
            query_fields = '{"Function": "Name","Table":"' + str(self.FTable) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return json.loads(response.text)['Result']
        except:
            print("Error: Name")
            return 0

    def FieldIndex(self,iName): 
        """
        Returns the index of the field name. A -1 result means the field does not exist      
        """
        try:
            query_fields = '{"Function": "FieldIndex","Table":"' + str(self.FTable) +  '","Field":"' + iName +  '"}'
            response = self.session.get(adb,params=query_fields)
            return json.loads(response.text)['Result']
        except:
            print("Error: FieldIndex")
            return 0

    def RecordCount(self): 
        """
        Returns the number of records in the table.
        Remember to use IsRecordAlive to ensure a record has not been deleted.
        """
        try:
            query_fields = '{"Function": "RecordCount","Table":"' + str(self.FTable) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return json.loads(response.text)['Result']
        except:
            print("Error: Name")
            return 0

    def GetDouble(self,iFld,iRec): 
        """
        Returns the index of the field name. A -1 result means the field does not exist      
        """
        try:
            query_fields = '{"Function": "GetDouble","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return json.loads(response.text)['Result']
        except:
            print("Error: GetDouble")
            return 0
        
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
        try:
            query_fields = '{"Function": "FieldName","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: FieldName")
            return 0
        
    def FieldCount(self): 
        """
        Returns the number of fields in the table      
        """        
        try:
            query_fields = '{"Function": "FieldCount","Table":"' + str(self.FTable) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: FieldCount")
            return 0

    def FieldType(self,iFld): 
        """
        Returns a string represenation of the field type    
        """
        try:
            query_fields = '{"Function": "FieldName","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: FieldType")
            return 0
        
    def IsRecordAlive(self,iRec): 
        """
        Returns a bool value where false implies the record does not exist anymore     
        """
        try:
            query_fields = '{"Function": "IsRecordAlive","Table":"' + str(self.FTable) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: IsRecordAlive")
            return 0
        
    def GetText(self,iFld,iRec): 
        try:
            query_fields = '{"Function": "GetText","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetText")
            return 0
        
    def GetInteger(self,iFld,iRec):   
        try:
            query_fields = '{"Function": "GetInteger","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetInteger")
            return 0

    def GetBool(self,iFld,iRec):  
        try:
            query_fields = '{"Function": "GetBool","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetBool")
            return 0    
        
    def GetPolyline(self,iFld,iRec) -> BaseGeometry:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            query_fields = '{"Function": "GetPolyline","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetPolyline")
            return 0
        
    def GetPolylineAll(self) -> list:  
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            query_fields = '{"Function": "GetPolylineAll","Table":"' + str(self.FTable) +  '"}'
            response = self.session.get(adb,params=query_fields)
            #print('Retrieved data')
            #with o pen('json_polyline.json', 'w') as outfile:
            #    outfile.write(response.text)
            allGeom = []
            data = json.loads(response.text)
            for line in data:
                allGeom.append(wkt.loads(data[line]))            
            return allGeom
        except:
            print("Error: GetPolylineAll")
            return 0
        
    def GetPoint(self,iFld,iRec) -> BaseGeometry: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            query_fields = '{"Function": "GetPoint","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetPoint")
            return 0

    def GetPolygon(self,iFld,iRec) -> BaseGeometry: 
        #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        try:
            query_fields = '{"Function": "GetPolygon","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '"}'
            response = self.session.get(adb,params=query_fields)
            return  wkt.loads(json.loads(response.text)['Result'])
        except:
            print("Error: GetPolygon")
            return 0
        
    def SetDouble(self,iFld,iRec,iValue):
        try:
            query_fields = '{"Function": "SetDouble","Table":"' + str(self.FTable) +  '","Field":"' + str(iFld) +  '","Record":"' + str(iRec) +  '","Value":"' + str(iValue) +  '"}'
            response = self.session.post(adb,params=query_fields)
            return  json.loads(response.text)['Result']
        except:
            print("Error: SetDouble")
            return 0
        
    def SetDoubleArray(self,iFld,iValues):
        try:
            query_fields = {
                    'Function': 'SetDoubleArray',
                    'Table': str(self.FTable),
                    'Field': str(iFld),
                    'Records':[]
                }

            for i in iValues:
                query_fields['Records'].append(i)
                
            text = json.dumps(query_fields)            
            
            #with open('json_data.json', 'w') as outfile:
            #    outfile.write(text)
            #print(text)
            
            response = self.session.post(adb,json=text)
            return  json.loads(response.text)['Result']
        except:
            print("Error: SetDoubleArray")
            return 0
        
    def SetPolyline(self,iRec,iValue):
        try:
            query_fields = '{"Function": "SetPolyline","Table":"' + str(self.FTable) + '","Record":"' + str(iRec) +  '","Value":"' + str(iValue) +  '"}'
            response = self.session.post(adb,params=query_fields)
            return  json.loads(response.text)['Result']
        except:
            print("Error: SetPolyline")
            return 0
    
'''
    def SetDouble(self,iFld,iRec,iValue):
        return adb.SetDouble(self.FTable, iFld, iRec, iValue) 

    def SetText(self,iFld,iRec,iValue): 
        return adb.SetText(self.FTable, iFld, iRec, iValue)

    def SetInteger(self,iFld,iRec,iValue):
        return adb.SetInteger(self.FTable, iFld, iRec, iValue)

    def SetBool(self,iFld,iRec,iValue): 
        return adb.SetBool(self.FTable, iFld, iRec, iValue)

    def SetPoint(self,iFld,iRec,iValue): 
        return adb.SetPoint(self.FTable,iFld,iRec,str(iValue))

    def SetPolyline(self,iFld,iRec,iValue: LineString):  
        return adb.SetPolyline(self.FTable,iFld,iRec,str(iValue))

    def SetPolygon(self,iFld,iRec,iValue): 
        return adb.SetPolygon(self.FTable,iFld,iRec,str(iValue))

    def AddRecord(self):
        return adb.AddRecord(self.FTable)

    def EraseRecord(self,iRec: int):
        return adb.EraseRecord(self.FTable,iRec)

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

    def Lock(self):
        return adb.Lock(self.FTable)

    def Flush(self):
        return adb.Flush(self.FTable)

    def EraseField(self,iField: int):
        return adb.EraseField(self.FTable,iField)

    def EraseAllRecords(self):
        return adb.EraseAllRecords(self.FTable)

    def Close(self):
        return adb.CloseTableAndDB(self.FTable)

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