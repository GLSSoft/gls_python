import GLS
import gls_python.adb as adb

model = GLS.Model

class Model:

  def __init__(self):
    self.FLayer = 0

  def BeginModelEvent(self):
    return model.BeginModelEvent()

  def EndModelEvent(self):
    return model.EndModelEvent()

  def GravityTable(self):
    return adb.AlbionDataBase(model.GravityTable())

  def RisingTable(self):
    return adb.AlbionDataBase(model.RisingTable())

  def StructureTable(self):
    return adb.AlbionDataBase(model.StructureTable())

  def PumpTable(self):
    return adb.AlbionDataBase(model.PumpTable())

  def DiversionTable(self):
    return adb.AlbionDataBase(model.DiversionTable())

  def UserHydrographTable(self):
    return adb.AlbionDataBase(model.UserHydrographTable())

  def AppurtenanceTable(self):
    return adb.AlbionDataBase(model.AppurtenanceTable())


