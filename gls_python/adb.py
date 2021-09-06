import GLS

adb = GLS.Adb

class AlbionDataBase:
    def __init__(self,iTable):
        self.FTable = iTable

    def Name(self):
        return adb.Name(self.FTable)

    def GetField(self,iFieldName):  
        return adb.GetField(self.FTable, iFieldName)

    def FieldIndex(self,iName): 
        return adb.FieldIndex(self.FTable, iName)

    def FieldName(self,iFld):  
        return adb.FieldName(self.FTable, iFld)

    def FieldCount(self): 
        return adb.FieldCount(self.FTable)

    def FieldType(self,iFld): 
        return adb.FieldType(self.FTable, iFld)

    def RecordCount(self): 
        return adb.RecordCount(self.FTable)

    def IsRecordAlive(self,iRec): 
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
