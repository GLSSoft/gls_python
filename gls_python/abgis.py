import GLS

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

  def GetTableFromLayer(self,layer):
    return gis.GetTableFromLayer(layer)
    
  def GetTableByLayerName(self,layername):
    return gis.GetTableByLayerName(layername)
    
  def GetTableByTableName(self,layername):	
    return gis.GetTableByTableName(layername)
