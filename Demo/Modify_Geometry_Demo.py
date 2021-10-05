import gls_python.wadiso as data
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt

def TestRoutine1():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    pipes = model.PipeTable()
    
    geom = pipes.FieldIndex('Geometry')
    for i in range(pipes.RecordCount()):
        line = pipes.GetPolyline(geom, i)
        print(line.length)       
        

if __name__ == "__main__":
    TestRoutine1()   