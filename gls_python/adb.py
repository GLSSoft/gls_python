import GLS
from shapely import wkt

adb = GLS.Adb

class AlbionDataBase:
        
    def __init__(self,iTable):
        self.FTable = iTable

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

