import GLS
import gls_python.adb as adb

#hook into the exposed wadiso model object
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
    '''
    Begin recording events on the active model, required to undo changes.
    NB call EndModelEvent after using this function
    '''
    return model.BeginModelEvent()

  @staticmethod
  def EndModelEvent():
    '''
    End recording events on the active model, required to undo changes
    NB this must be called after using BeginModelEvent
    '''
    return model.EndModelEvent()

  @staticmethod
  def NodeTable():
    return adb.AlbionDataBase(model.NodeTable())

  @staticmethod
  def SourceTable():
    return adb.AlbionDataBase(model.SourceTable())

  @staticmethod
  def ValveTable():
    return adb.AlbionDataBase(model.ValveTable())

  @staticmethod
  def PipeTable():
    return adb.AlbionDataBase(model.PipeTable())

  @staticmethod
  def PumpTable():
    return adb.AlbionDataBase(model.PumpTable())
    
  @staticmethod
  def AppurtenanceTable():
    return adb.AlbionDataBase(model.AppurtenanceTable())

