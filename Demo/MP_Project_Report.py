import gls_python.wadiso as data
import gls_python.adb as adb
import gls_python.abgis as gis 
import gls_python.general as general
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt
import gmplot
import pandas as pd
import os

def RenderOnField_Plot(iField):
    # Get the active model
    model = data.Model()

    links = []
    links.append(model.PipeTable())
    links.append(model.PumpTable())
    links.append(model.ValveTable())

    nodes = []
    nodes.append(model.SourceTable())

    
    # Get all unique projects
    distinctValues = []
    for item in links:
        print(item.Name())
        fldMPProject = item.FieldIndex("MP_Project_No")  
        tempValues = item.GetDistinctTextValuesNaturalSort(fldMPProject) 
        for mpProj in tempValues:
            if not mpProj in distinctValues:
                if len(mpProj)> 0:
                    distinctValues.append(mpProj)

    for mpProj in distinctValues:
        print("Item: " + mpProj)
        for link in links:   
            fldGeom = link.FieldIndexGeom()     
            fldMPProject = link.FieldIndex("MP_Project_No") 
            if  fldMPProject != -1 and fldGeom != -1:  
                records = link.RecordsFromValue(fldMPProject, mpProj)
                for i in records:
                    line = link.GetPolyline(fldGeom, i)  
                    x,y = line.xy
                    plt.plot(x, y) 

        for node in nodes: 
            fldGeom = node.FieldIndex("Geometry")     
            fldMPProject = node.FieldIndex("MP_Project_No")       
            records = node.RecordsFromValue(fldMPProject, mpProj)
            for i in records:
                point = link.GetPoint(fldGeom, i)  
                x,y = point.xy
                plt.plot(x, y) 
    
        plt.savefig("D:\\Work\\Report\\" + mpProj + ".png")
        plt.clf()
        plt.cla()
        plt.close()

def RenderOnField_HTML(iClient,iModel,iFieldName):
    # Get the active model
    model = data.Model()

    links = []
    links.append(model.PipeTable())
    links.append(model.PumpTable())
    links.append(model.ValveTable())

    nodes = []
    nodes.append(model.SourceTable())

    
    # Get all unique projects
    distinctValues = []
    for item in links:
        print(item.Name())
        iField = item.FieldIndex(iFieldName)  
        tempValues = item.GetDistinctTextValuesNaturalSort(iField) 
        for mpProj in tempValues:
            if not mpProj in distinctValues:
                if len(mpProj)> 0:
                    distinctValues.append(mpProj)

    for mpProj in distinctValues: 
        gmap = gmplot.GoogleMapPlotter(-33.981067, 22.453469, 14, apikey="")

        for link in links: 
            fldGeom = link.FieldIndexGeom()     
            fldMPProject = link.FieldIndex(iFieldName) 
            if  fldMPProject != -1 and fldGeom != -1:  
                records = link.RecordsFromValue(fldMPProject, mpProj)

                progress = general.ProgressBar("Rendering MP Projects...", link.RecordCount())

                for i in records:  
                    arrayx = [] 
                    arrayy = []

                    x_arr,y_arr = link.GetPolyline(fldGeom, i).xy
                    for x in x_arr:
                        arrayx.append(x)    
                    for y in y_arr:
                        arrayy.append(y) 
                        
                    gmap.scatter( arrayy, arrayx, '#FF0000',size = 1, marker = False )                    
                    gmap.plot(lats=arrayy,lngs=arrayx,color='cornflowerblue',edge_width=2, cickable = True)

                    progress.Increment()

                progress.Close()

        path = "D:/Work/Report/"+iClient+ "/"+iModel+"/Maps/"+iFieldName
        if not os.path.isdir(path):
            os.makedirs(path,mode = 0o666)
            print("Created: " + path)

        new = mpProj.replace("/", "_")
        new = new.replace("\\", "_")
        gmap.draw(path + "/" + new + ".html")    

    general.ShowNotification("Finished map " + iFieldName, 10 )

def ReportFieldName(iClient,iModel,iFieldName):
    model = data.Model()

    pipe = model.PipeTable()

    fldIndex = pipe.FieldIndex(iFieldName)
    fldLengths = pipe.FieldIndex("Length")
    fldAverage = pipe.FieldIndex("Diameter")

    vDataName = []
    vDataLength = []
    vDataAverage = []

    systems = pipe.GetDistinctTextValuesNaturalSort(fldIndex)
    for str in systems:
        records = pipe.RecordsFromValue(fldIndex, str)

        vLength = 0
        vAverage = 0
        for vRec in records:
            vLength = vLength + pipe.GetDouble(fldLengths,vRec)
            vAverage = vAverage + pipe.GetDouble(fldAverage,vRec)

        vAverage = vAverage / len(records)

        vDataName.append(str)
        vDataLength.append(vLength)
        vDataAverage.append(vAverage)

    # creating the dataframe
    df = pd.DataFrame({iFieldName: vDataName,
                        "Lengths": vDataLength,
                        "Average": vDataAverage})

    result = df.to_html()

    path = "D:/Work/Report/"+iClient+ "/"+iModel+"/Data/"
    if not os.path.isdir(path):
        os.makedirs(path,mode = 0o666)
        print("Created: " + path)

    textfile = open((path + "/" + iFieldName+".html")  , "w")

    a = textfile.write(result)
    textfile.close()

    general.ShowNotification("Finished data " + iFieldName, 10 )

if __name__ == "__main__":
    RenderOnField_HTML("Client","George","MP_Project_No")
    RenderOnField_HTML("Client","George","System")
    RenderOnField_HTML("Client","George","Suburb")
    RenderOnField_HTML("Client","George","Future_System")

    ReportFieldName("Client","George","MP_Project_No")
    ReportFieldName("Client","George","System")
    ReportFieldName("Client","George","Suburb")
    ReportFieldName("Client","George","Future_System")