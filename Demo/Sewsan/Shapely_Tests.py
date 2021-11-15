from gls_python import sewsan
from gls_python import adb
from gls_python.adb import AlbionDataBase
from gls_python import general
from gls_python import abgis as gis
from shapely.geometry import Point, multipoint
from shapely.ops import triangulate
from shapely.ops import voronoi_diagram
#from shapely.ops import voronoi_diagram

def GetTableByName(iName):
    layers = gis.AlbionGisLayer()

    for i in range(layers.GetLayerCount()):
        layer = layers.GetLayerByIndex(i)
        table = layers.GetTableFromLayerIndex(layer)
        if iName in table.Name():
            return table
    
    general.ShowNotification(iName + " not found", general.AlbionMessageTypes.ntError)
    return None 


def Delaunay_Triangulation(points_table: AlbionDataBase):
    fldPoint = points_table.FieldIndexGeom()
    points = []
    for i in range(points_table.RecordCount()):
        if points_table.IsRecordAlive(i):
            points.append(points_table.GetPoint(fldPoint,i))

    multi = multipoint.MultiPoint(points)

    regions = triangulate(multi)

    data = GetTableByName("Layer")
    data.AddField("Geometry", adb.AlbionFieldTypes.AdbFTGeomPolygon)

    fldPoly = data.FieldIndexGeom()

    for region in regions:
        print(region.exterior.coords)
        rec = data.AddRecord()
        data.SetPolygon(fldPoly, rec, region)

    print(data.Name())
    gis.AlbionGisLayer().RefreshRendering()

def Voronoi_Diagram(points_table: AlbionDataBase):
    fldPoint = points_table.FieldIndexGeom()
    points = []
    for i in range(points_table.RecordCount()):
        if points_table.IsRecordAlive(i):
            points.append(points_table.GetPoint(fldPoint,i))

    multi = multipoint.MultiPoint(points)

    regions = voronoi_diagram(multi)

    data = GetTableByName("Layer")
    data.AddField("Geometry", adb.AlbionFieldTypes.AdbFTGeomPolygon)

    fldPoly = data.FieldIndexGeom()

    for region in regions:
        print(region.exterior.coords)
        rec = data.AddRecord()
        data.SetPolygon(fldPoly, rec, region)

    print(data.Name())
    gis.AlbionGisLayer().RefreshRendering()

if __name__ == "__main__":
    Delaunay_Triangulation(sewsan.Model().StructureTable())  
    Voronoi_Diagram(sewsan.Model().StructureTable())  