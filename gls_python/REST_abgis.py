from REST_GLS_Interface import GLS_REST_INTERFACE as GLS_Interface
from REST_GLS_Interface import bcolors as bcolors
import inspect
from REST_adb import AlbionDataBase as abDB

gis = "http://127.0.0.1:8080/GLS_GIS/"

class AlbionGisLayer:

  def __init__(self):
    pass  
       
  @staticmethod    
  def GetSetMethod(iFunc,iAction=-1,iRaw=False):
      try:
          query_fields = {
              "Function":iFunc,
              "Action":iAction
              }
                        
          return GLS_Interface.AlbionPOST(gis,query_fields,iRaw)     
      except:
          bcolors.print_fail("Error: " + iFunc)
          return 0
          
  @staticmethod
  def GetAllTables() -> list:
    result = []
    layers = AlbionGisLayer.GetAllLayers()
    for layer in layers:
      result.append(abDB(AlbionGisLayer.GetTableFromLayer(layer)))
    return result
          
  @staticmethod
  def GetAllLayers() -> list:
    result = []
    count = AlbionGisLayer.GetLayerCount()
    for i in range(count):
      result.append(AlbionGisLayer.GetLayerByIndex(i))
    return result
          
  @staticmethod
  def GetAllTableNames() -> list:
    result = []  
    for tab in AlbionGisLayer.GetAllTables():
      result.append(tab.Name())
    return result
          
  @staticmethod
  def GetAllLayerNames() -> list:
    result = []  
    for layer in AlbionGisLayer.GetAllLayers():
      result.append(AlbionGisLayer.GetLayerName(layer))
    return result
  
  @staticmethod
  def PrintLayerNames():  
    for name in AlbionGisLayer.GetAllLayerNames():
      bcolors.print_cyan(name)
  
  @staticmethod
  def PrintTableNames():     
    OKCYAN = '\033[96m' 
    ENDC = '\033[0m'  
    for name in AlbionGisLayer.GetAllTableNames():  
      bcolors.print_green(name)        
    
  @staticmethod
  def GetLayerByIndex(index):
      return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,str(index))  

  @staticmethod
  def GetLayerCount():
      return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name)

  @staticmethod
  def GetLayerName(layer):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,str(layer))

  @staticmethod
  def GetTableFromLayer(layer):    
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,str(layer))  

  @staticmethod
  def CommandLine(iFunction):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,iFunction)  

  @staticmethod
  def RefreshRendering():
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name)  

  @staticmethod
  def GetLayerByIndex(index):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,index)  

  @staticmethod
  def GetLayerName(layer):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,layer)  
  
  @staticmethod
  def GetTableFromLayer(layer):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,layer)  
  
  @staticmethod
  def GetTableByLayerName(name):
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name,name)  
  
  @staticmethod
  def TablePicker():
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name)  
  
  @staticmethod
  def LayerPicker():
    return AlbionGisLayer.GetSetMethod(inspect.currentframe().f_code.co_name)  
