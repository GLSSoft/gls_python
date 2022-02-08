from argparse import Action
from abgis import AlbionGisLayer as AbGIS
from adb import AlbionDataBase as Adb 
from tqdm import tqdm
from wadiso import Model as activemodel

import matplotlib.pyplot as plt

from tqdm import tqdm

def TestRoutine1():

    layer = AbGIS.GetLayerByIndex(5)
    print(AbGIS.GetLayerName(layer))
    table = AbGIS.GetTableFromLayer(layer)
    pipes = Adb(table)
    print(pipes.Name())
    
    #https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    
    geom = pipes.GetPolylineAll()

    for i in tqdm(range(len(geom))):
        x, y = geom[i].xy   
       #     if pipes.SetPolyline(i,geom[i]) != 0:
       #         print("Error")
        plt.plot(x, y)

    activemodel.BeginModelEvent()
    try:
        fld = pipes.FieldIndex("Diameter")
        arr = []
        for i in tqdm(range(pipes.RecordCount())):
            arr.append(200)
            
        pipes.SetDoubleArray(fld,arr)
    finally:
        activemodel.EndModelEvent()
         

    # Add title
    plt.title("WGS84 projection")

    # Remove empty white space around the plot
    plt.tight_layout()  

    plt.show()

if __name__ == "__main__":
    TestRoutine1()  