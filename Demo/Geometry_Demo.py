import gls_python.wadiso as data
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt

def TestRoutine1():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    pipes = model.PipeTable()                                  
    pumps = model.PumpTable()
    valves = model.ValveTable()   
    nodes = model.NodeTable()
    sources = model.SourceTable()
    
    geom = pipes.FieldIndex('Geometry')
    for i in range(pipes.RecordCount()):
        x, y = pipes.GetPolyline(geom, i).xy
        plt.plot(x, y)  
        
    geom = pumps.FieldIndex('Geometry')
    for i in range(pumps.RecordCount()):
        x, y = pumps.GetPolyline(geom, i).xy
        plt.plot(x, y)      
        
    geom = valves.FieldIndex('Geometry')
    for i in range(valves.RecordCount()):
        x, y = valves.GetPolyline(geom, i).xy
        plt.plot(x, y)   
        
    geom = nodes.FieldIndex('Geometry')
    for i in range(nodes.RecordCount()):
        x, y = nodes.GetPoint(geom, i).xy
        plt.plot(x, y)   
        
    geom = sources.FieldIndex('Geometry')
    for i in range(sources.RecordCount()):
        x, y = sources.GetPoint(geom, i).xy
        plt.plot(x, y) 

    # Plot the WGS84
    #data.plot(facecolor='gray');

    # Add title
    plt.title("WGS84 projection")

    # Remove empty white space around the plot
    plt.tight_layout()  

    plt.show()

if __name__ == "__main__":
    TestRoutine1()  