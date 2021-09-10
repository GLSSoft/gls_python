import gls_python.wadiso as data
import gls_python.adb as adb
import gls_python.abgis as gis 
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt

def CopyLinks():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    pipes = model.PipeTable()    
    geom = pipes.FieldIndex('Geometry')

    # Create a new Albion table, it will not be visible until added to
    # the GIS layer manager
    newTable = adb.AlbionDataBase()
    # Create the table
    newTable.CreateTable('Line_Copy')
    #Add an id field of type guid
    newTable.AddField('id',7)
    #Add a polyline field
    fldgeom = newTable.AddField('Geometry',34)

    for i in range(pipes.RecordCount()):
        line = pipes.GetPolyline(geom, i)  
        if i % 3 == 0:
            newrec = newTable.AddRecord() 
            newTable.SetPolyline(fldgeom,newrec,line)  

    # Create gis layer class
    gisClass = gis.AlbionGisLayer()    
    gisClass.AddTableToGIS(newTable.Pointer())     
    gisClass.RefreshRendering()   

def CopyNodes():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    nodes = model.NodeTable()    
    geom = nodes.FieldIndex('Geometry')

    # Create a new Albion table, it will not be visible until added to
    # the GIS layer manager
    newTable = adb.AlbionDataBase()
    # Create the table
    newTable.CreateTable('Node_Copy')
    #Add an id field of type guid
    newTable.AddField('id',7)
    #Add a polyline field
    fldgeom = newTable.AddField('Geometry',32)

    for i in range(nodes.RecordCount()):
        line = nodes.GetPoint(geom, i)  
        if i % 3 == 0:
            newrec = newTable.AddRecord() 
            newTable.SetPoint(fldgeom,newrec,line)  

    # Create gis layer class
    gisClass = gis.AlbionGisLayer()    
    gisClass.AddTableToGIS(newTable.Pointer())     
    gisClass.RefreshRendering()   

def BufferLinks():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    pipes = model.PipeTable()    
    geom = pipes.FieldIndex('Geometry')

    # Create a new Albion table, it will not be visible until added to
    # the GIS layer manager
    newTable = adb.AlbionDataBase()
    # Create the table
    newTable.CreateTable('Line_Buffer')
    #Add an id field of type guid
    newTable.AddField('id',7)
    #Add a polyline field
    fldgeom = newTable.AddField('Geometry',35)

    for i in range(pipes.RecordCount()):
        line = pipes.GetPolyline(geom, i)  
        newrec = newTable.AddRecord() 
        buffer = line.buffer(2.0)
        newTable.SetPolygon(fldgeom,newrec,buffer)  
        x,y = buffer.exterior.xy
        plt.plot(x, y) 

    # Create gis layer class
    gisClass = gis.AlbionGisLayer()    
    gisClass.AddTableToGIS(newTable.Pointer())     
    gisClass.RefreshRendering()  

def RenderChart():     
    # Remove empty white space around the plot
    plt.tight_layout()  

    plt.show()

if __name__ == "__main__":
    CopyLinks() 
    CopyNodes()
    BufferLinks()
    RenderChart()