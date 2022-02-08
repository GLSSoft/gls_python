from abgis import AlbionGisLayer as AbGIS
from adb import AlbionDataBase as Adb
from wadiso import Model as activemodel

try:     
    print( activemodel.ModelName() )
    print( activemodel.PumpTable().Name())
    
    tables = activemodel.AllTables()
    for tab in tables:
        print(tab.Name())
    
    #print(AbGIS.GetLayerCount())    
    
    #for i in range(AbGIS.GetLayerCount()):
    #    print(str(i))
    #    layer = AbGIS.GetLayerByIndex(i)
    #    print(AbGIS.GetLayerName(layer))
    #    table = AbGIS.GetTableFromLayer(layer)
    #    albiontable = Adb(table)
    #    print(albiontable.Name())
        
        
        
    #layer = AbGIS.GetLayerByIndex(2)
    #print(AbGIS.GetLayerName(layer))
    
    #AbGIS.CommandLine('Wadiso.BalanceModel')
    
except:
    print("Error")