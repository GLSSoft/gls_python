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

  def SubstationTable(self):
    return adb.AlbionDataBase(model.SubstationTable())

  def SourceTable(self):
    return adb.AlbionDataBase(model.SourceTable())

  def SourceTableInternal(self):
    return adb.AlbionDataBase(model.SourceTableInternal())

  def NodeTable(self):
    return adb.AlbionDataBase(model.NodeTable())

  def NodeTableInternal(self):
    return adb.AlbionDataBase(model.NodeTableInternal())
    
  def BreakerTable(self):
    return adb.AlbionDataBase(model.BreakerTable())
    
  def BreakerTableInternal(self):
    return adb.AlbionDataBase(model.BreakerTableInternal())
    
  def SupplyPointTable(self):
    return adb.AlbionDataBase(model.SupplyPointTable())
    
  def SupplyPointTableInternal(self):
    return adb.AlbionDataBase(model.SupplyPointTableInternal())
    
  def LoadTable(self):
    return adb.AlbionDataBase(model.LoadTable())
    
  def LoadTableInternal(self):
    return adb.AlbionDataBase(model.LoadTableInternal())
    
  def ConductorTable(self):
    return adb.AlbionDataBase(model.ConductorTable())
    
  def ConductorTableInternal(self):
    return adb.AlbionDataBase(model.ConductorTableInternal())
    
  def AppurtenanceTable(self):
    return adb.AlbionDataBase(model.AppurtenanceTable())
    
  def AppurtenanceTableInternal(self):
    return adb.AlbionDataBase(model.AppurtenanceTableInternal())
    
  def FaultLocationTable(self):
    return adb.AlbionDataBase(model.FaultLocationTable())
    
  def FaultLocationTableInternal(self):
    return adb.AlbionDataBase(model.FaultLocationTableInternal())
    
  def TransformerTableInternal(self):
    return adb.AlbionDataBase(model.TransformerTableInternal())
    
  def CapacitorInternal(self):
    return adb.AlbionDataBase(model.CapacitorInternal())
    
  def BusNodeInternal(self):
    return adb.AlbionDataBase(model.BusNodeInternal())
    
  def BusBarInternal(self):
    return adb.AlbionDataBase(model.BusBarInternal())
    
  def IWConnectionInternal(self):
    return adb.AlbionDataBase(model.IWConnectionInternal())

