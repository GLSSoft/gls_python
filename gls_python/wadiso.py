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

  def NodeTable(self):
    return adb.AlbionDataBase(model.NodeTable())

  def SourceTable(self):
    return adb.AlbionDataBase(model.SourceTable())

  def ValveTable(self):
    return adb.AlbionDataBase(model.ValveTable())

  def PipeTable(self):
    return adb.AlbionDataBase(model.PipeTable())

  def PumpTable(self):
    return adb.AlbionDataBase(model.PumpTable())
    
  def AppurtenanceTable(self):
    return adb.AlbionDataBase(model.AppurtenanceTable())
