import GLS
import gls_python.adb as adb

model = GLS.Model

class Model:

  def __init__(self):
    pass

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


