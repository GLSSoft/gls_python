import GLS

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
  def NodeTable():
    return model.NodeTable()

  @staticmethod
  def LinkTable():
    return model.LinkTable()
    
  @staticmethod
  def AppurtenanceTable():
    return model.AppurtenanceTable()
  