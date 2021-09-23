from gls_python import sewsan
from gls_python import adb

def ShowData(iTable: adb.AlbionDataBase):
    print(iTable.Name() + " - " + str(iTable.RecordCount()))

def FunctionToRun():

    model = sewsan.Model()

    ShowData(model.GravityTable())

    ShowData(model.RisingTable())

    ShowData(model.StructureTable())

    ShowData(model.PumpTable())

    ShowData(model.DiversionTable())
        
    ShowData(model.UserHydrographTable())
        
    ShowData(model.AppurtenanceTable())    

if __name__ == "__main__":
    FunctionToRun()