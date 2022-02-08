import requests
import json

#gis = "http://localhost:8080/GLS_GIS/"
gis = "http://127.0.0.1:8080/GLS_GIS/"

class AlbionGisLayer:

  def __init__(self):
    pass
    
  @staticmethod
  def GetLayerByIndex(index):
    try:
        query_fields = '{"Function": "GetLayerByIndex","Action":"' + str(index) +  '"}'
        response = requests.get(gis,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: GetLayerByIndex")
        return 0

  @staticmethod
  def GetLayerCount():
    try:
        query_fields = '{"Function":"GetLayerCount"}'  
        response = requests.get(gis,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: GetLayerCount")
        return 0

  @staticmethod
  def GetLayerName(layer):
    try:
        query_fields = '{"Function":"GetLayerName","Action":"' + str(layer) +  '"}'
        response = requests.get(gis,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: GetLayerName")
        return 0

  @staticmethod
  def GetTableFromLayer(layer):      
    try:
        query_fields = '{"Function":"GetTableFromLayer","Action":"' + str(layer) +  '"}'
        response = requests.get(gis,params=query_fields)
        return json.loads(response.text)['Result']
    except:
        print("Error: GetTableFromLayer")
        return 0

  @staticmethod
  def CommandLine(iFunction):
    try:
        query_fields = '{"Function":"CommandLine","Action":"' + iFunction +  '"}'
        requests.get(gis,params=query_fields)
    except:
        print("Error: CommandLine")
        return 0
