import GLS
import gls_python.adb as adb

gis = GLS.Gis

class AlbionGisLayer:

  def __init__(self):
    self.FLayer = 0

  def GetLayerCount(self):
    return gis.GetLayerCount()

  def GetLayerByIndex(self,index):
    return gis.GetLayerByIndex(index)

  def GetLayerName(self,layer):
    return gis.GetLayerName(layer)

  def GetTableFromLayerIndex(self,layer):
    return adb.AlbionDataBase(gis.GetTableFromLayer(layer))
    
  def GetTableByLayerName(self,layername):
    return adb.AlbionDataBase(gis.GetTableByLayerName(layername))
    
  def GetTableByTableName(self,layername):	
    return adb.AlbionDataBase(gis.GetTableByTableName(layername))

  def AddTableToGIS(self,iTable):  
    return gis.AddTableToGIS(iTable)

  def RefreshRendering(self):
    gis.RefreshRendering()

  def CommandLine(self, iFunction):
    gis.CommandLine(iFunction)
