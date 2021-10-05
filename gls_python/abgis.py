import GLS
import gls_python.adb as adb

gis = GLS.Gis

class AlbionGisLayer:

  def __init__(self):
    pass

  @staticmethod
  def GetLayerCount():
    return gis.GetLayerCount()

  @staticmethod
  def RefreshRendering():
    gis.RefreshRendering()

  @staticmethod
  def CommandLine(iFunction):
    gis.CommandLine(iFunction)

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
    
  def TablePicker(self,message):  
    return adb.AlbionDataBase(gis.TablePicker(message))

  def AddTableToGIS(self,iTable):  
    return gis.AddTableToGIS(iTable)
