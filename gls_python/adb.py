import GLS
from shapely import wkt
from shapely.geometry import Point, LineString, Polygon

adb = GLS.Adb

class AlbionDataBase:
        
    def __init__(self,iTable=-1):
        if iTable != -1:
            self.FTable = iTable

    def CreateTable(self,iName):
        self.FTable = adb.CreateTable(iName)

    def Pointer(self):
        return self.FTable

    def Name(self):
        """
        Returns the table name of the current object     
        """
        return adb.Name(self.FTable)

    def FieldIndex(self,iName): 
        """
        Returns the index of the field name. A -1 result means the field does not exist      
        """
        return adb.FieldIndex(self.FTable, iName)

    def FieldName(self,iFld):  
        """
        Returns the name of the field at the current index. An invalid number will cause an error
        Use fieldindex to get a proper index      
        """
        return adb.FieldName(self.FTable, iFld)

    def FieldCount(self): 
        """
        Returns the number of fields in the table      
        """
        return adb.FieldCount(self.FTable)

    def FieldType(self,iFld): 
        """
        Returns a string represenation of the field type    
        """
        return adb.FieldType(self.FTable, iFld)

    def RecordCount(self): 
        """
        Returns the number of records in the table.
        Remember to use IsRecordAlive to ensure a record has not been deleted.
        """
        return adb.RecordCount(self.FTable)

    def IsRecordAlive(self,iRec): 
        """
        Returns a bool value where false implies the record does not exist anymore     
        """
        return adb.IsRecordAlive(self.FTable, iRec)

    def GetDouble(self,iFld,iRec): 
        return adb.GetDouble(self.FTable, iFld, iRec)

    def GetText(self,iFld,iRec): 
        return adb.GetText(self.FTable, iFld, iRec)

    def GetInteger(self,iFld,iRec):   
        return adb.GetInteger(self.FTable, iFld, iRec)

    def GetBool(self,iFld,iRec):  
        return adb.GetBool(self.FTable, iFld, iRec)

    def SetDouble(self,iFld,iRec,iValue):
        return adb.SetDouble(self.FTable, iFld, iRec, iValue) 

    def SetText(self,iFld,iRec,iValue): 
        return adb.SetText(self.FTable, iFld, iRec, iValue)

    def SetInteger(self,iFld,iRec,iValue):
        return adb.SetInteger(self.FTable, iFld, iRec, iValue)

    def SetBool(self,iFld,iRec,iValue): 
        return adb.SetBool(self.FTable, iFld, iRec, iValue)

    def RecordsFromValue(self,iFld,iValue):
        return adb.RecordsFromValue(self.FTable,iFld,iValue)

    def GetPoint(self,iFld,iRec): 
        return wkt.loads(adb.GetPoint(self.FTable,iFld,iRec))

    def GetPolyline(self,iFld,iRec):  
        return wkt.loads(adb.GetPolyline(self.FTable,iFld,iRec))

    def GetPolygon(self,iFld,iRec): 
        return wkt.loads(adb.GetPolygon(self.FTable,iFld,iRec))

    def SetPoint(self,iFld,iRec,iValue): 
        return adb.SetPoint(self.FTable,iFld,iRec,str(iValue))

    def SetPolyline(self,iFld,iRec,iValue: LineString):  
        return adb.SetPolyline(self.FTable,iFld,iRec,str(iValue))

    def SetPolygon(self,iFld,iRec,iValue): 
        return adb.SetPolygon(self.FTable,iFld,iRec,str(iValue))

    def AddRecord(self):
        return adb.AddRecord(self.FTable)

    def EraseRecord(self,iRec):
        return adb.EraseRecord(self.FTable,iRec)

    def AddField(self,iName,iType):
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
        return adb.AddField(self.FTable,iName,iType)


    def Close(self):
        return adb.CloseTableAndDB(self.FTable)
