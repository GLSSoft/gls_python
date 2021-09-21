import gls_python.wadiso as data
import gls_python.adb as adb
import gls_python.abgis as gis 
from shapely.geometry import Point, LineString, Polygon
from shapely.strtree import STRtree
import random
import gls_python.general as general

dummyPointsTable = adb.AlbionDataBase()
model = data.Model()

maxX = -9999999
maxY = -9999999
minX = 9999999
minY = 9999999

spatialTree = ""
index_by_id = {}

def GetModelBounds():
    global maxX
    global maxY
    global minX
    global minY

    table = model.NodeTable()
    fldGeom = table.FieldIndex("Geometry")


    for iRec in range(table.RecordCount()):
        x,y = table.GetPoint(fldGeom, iRec).xy
        if maxX < x[0]:
            maxX = x[0]
        if x[0] < minX:
            minX = x[0]

        if maxY < y[0]:
            maxY = y[0]
        if y[0] < minY:
            minY = y[0]   

    print(str(maxX) + " " + str(minX) + " " + str(maxY) + " " + str(minY))


def CreateDummyPoints():
    
    global maxX
    global maxY
    global minX
    global minY  
    global dummyPointsTable  

    print(str(maxX) + " " + str(minX) + " " + str(maxY) + " " + str(minY))

    # Create the table
    dummyPointsTable.CreateTable('DummyPoints')  
    fldGeom = dummyPointsTable.AddField('Geometry',32)
    fldNearestLink = dummyPointsTable.AddField('Nearest',5)

    numberOfpoints = 100
    for i in range(numberOfpoints):
        x = random.randint(int(minX),int(maxX))
        y = random.randint(int(minY),int(maxY))

        p = Point(x,y)
        newRec = dummyPointsTable.AddRecord()
        dummyPointsTable.SetPoint(fldGeom,newRec,p)

    gisClass = gis.AlbionGisLayer()    
    gisClass.AddTableToGIS(dummyPointsTable.Pointer())     
    gisClass.RefreshRendering()   

def CreateRTree():
    global index_by_id
    global spatialTree 

    table = model.NodeTable()
    fldGeom = table.FieldIndex("Geometry")
    geomData = []
    
    for iRec in range(table.RecordCount()):
        p = table.GetPoint(fldGeom, iRec)
        geomData.append(p)
        index_by_id[id(p)] = iRec

    spatialTree = STRtree(geomData)

def FindClosest():    
    global spatialTree 
    global index_by_id

    table = model.NodeTable()
    fldNode = table.FieldIndex("Node_Code")

    resultTable = adb.AlbionDataBase()
    resultTable.CreateTable('Results')  
    fldGeom = resultTable.AddField('Geometry',34)

    fldDummy = dummyPointsTable.FieldIndex("Geometry")    
    fldCode = dummyPointsTable.FieldIndex("Nearest")

    progBar = general.ProgressBar("Finding closest...", dummyPointsTable.RecordCount())
    for iRec in range(dummyPointsTable.RecordCount()):
        p = dummyPointsTable.GetPoint(fldDummy,iRec)
        px,py = p.xy  
        n = spatialTree.nearest(p)      
        nx,ny = n.xy
        line = LineString([(px[0], py[0]),(nx[0], ny[0])])

        newRec = resultTable.AddRecord()
        resultTable.SetPolyline(fldGeom, newRec, line)

        dummyPointsTable.SetText(fldCode, iRec, table.GetText(fldNode, index_by_id[id(n)])) 

        progBar.Increment()

    progBar.Close()

    gisClass = gis.AlbionGisLayer()    
    gisClass.AddTableToGIS(resultTable.Pointer()) 
    gisClass.RefreshRendering()  

if __name__ == "__main__":
    GetModelBounds() 
    CreateDummyPoints()
    CreateRTree()
    FindClosest()

    general.ShowNotification("Complete",1)  
    