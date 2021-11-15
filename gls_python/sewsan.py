import GLS
import gls_python.adb as adb

model = GLS.Model

class Model:

  def __init__(self):
    pass

  @staticmethod
  def LoadModel(filename: str):
    '''
    Load the model at the specified location as the active model
    '''
    model.LoadModel(filename)

  @staticmethod
  def CloseModel():
    '''
    Close the current active model
    '''
    model.CloseModel()

  @staticmethod
  def SwitchActiveModel():
    '''
    Launch the model display control UI
    '''
    model.SwitchActiveModel()
    
  @staticmethod
  def ModelName():
    '''
    Returns the active model's name
    '''
    return model.ModelName()
    
  @staticmethod
  def ModelPath():
    '''
    Returns the active models connection string
    '''
    return model.ModelPath()

  @staticmethod
  def AllTables() -> list:
    allTables = []
    tables = model.AllBaseDataUnits()
    for i in tables:
      allTables.append(adb.AlbionDataBase(i))
    return allTables

  @staticmethod
  def BeginModelEvent():
    return model.BeginModelEvent()

  @staticmethod
  def EndModelEvent():
    return model.EndModelEvent()

  @staticmethod
  def GravityTable():
    return adb.AlbionDataBase(model.GravityTable())

  @staticmethod
  def RisingTable():
    return adb.AlbionDataBase(model.RisingTable())

  @staticmethod
  def StructureTable():
    return adb.AlbionDataBase(model.StructureTable())

  @staticmethod
  def PumpTable():
    return adb.AlbionDataBase(model.PumpTable())

  @staticmethod
  def DiversionTable():
    return adb.AlbionDataBase(model.DiversionTable())

  @staticmethod
  def UserHydrographTable():
    return adb.AlbionDataBase(model.UserHydrographTable())

  @staticmethod
  def AppurtenanceTable():
    return adb.AlbionDataBase(model.AppurtenanceTable())


