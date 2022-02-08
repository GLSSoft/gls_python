import pandas as pd     
import seaborn as sborn    
from tqdm import tqdm
import matplotlib.pyplot as plt

from abgis import AlbionGisLayer as AbGIS
from adb import AlbionDataBase as Adb


import time

import requests

def TestRoutine1():
    session = requests.Session()
    
    start = time.time()
    layer = AbGIS.GetLayerByIndex(5)
    print(AbGIS.GetLayerName(layer))
    table = AbGIS.GetTableFromLayer(layer)
    albiontable = Adb(table)
    print(albiontable.Name())

    # Get the diameter field index
    diameterField = albiontable.FieldIndex('Diameter')
    fldLength = albiontable.FieldIndex('Length')

    # Create lists
    listOfDiameters = []
    lengths = []

    for i in tqdm(range(albiontable.RecordCount())):
        #albiontable.SetDouble(diameterField,i,12.0)
        listOfDiameters.append(albiontable.GetDouble(diameterField,i)) 
        lengths.append(albiontable.GetDouble(fldLength,i))

    list_of_tuples = list(zip(listOfDiameters, lengths))

    df = pd.DataFrame(list_of_tuples, columns = ['Size', 'Length'])   
    #sborn.boxplot(x="Size", y="Length", data=df)
    plt.scatter(df['Size'], df['Length'])
    
    print(time.time() - start) # before showing the graph
    
    plt.show()

if __name__ == "__main__":
    TestRoutine1()  