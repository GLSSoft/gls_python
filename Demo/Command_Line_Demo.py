import gls_python.abgis as gis
import gls_python.wadiso as wadiso

import csv
import random

import seaborn as sns
import pandas as pd         
import matplotlib.pyplot as plt

import gls_python.general as general

def TestRoutine1():
    layer = gis.AlbionGisLayer()
    model = wadiso.Model()
    nodes = model.NodeTable()
    valves = model.ValveTable()

    fldHead = nodes.FieldIndex("Head")
    fldCode = nodes.FieldIndex("Node_Code")
    fldOpen = valves.FieldIndex("Valve_Status")

    allResults = []    

    listofnodes = []
    listofnodepressure = []
    basepressures = []
    basecodes = []

    listOfNodesToCheck = ["16685","19310","13166","10883","15323"]
    for str in listOfNodesToCheck:
        general.ShowNotification("Checking " + str, 10)        
        allResults.append([])

    iterations = 2
    progbar = general.ProgressBar("Analyising...", iterations)
    for i in range(iterations):
        print(i)
        general.CommandLine("Wadiso.BalanceModel")
        progbar.Increment()
        count = 0
        newResult = []
        for iRec in range(nodes.RecordCount()):
            
            if nodes.IsRecordAlive(iRec):              
                nodeCode = nodes.GetText(fldCode, iRec)
                if nodeCode in listOfNodesToCheck:

                    pressure = nodes.GetDouble(fldHead,iRec)
                    if pressure > 120: 
                        pressure = 120
                    elif pressure < 0:
                        pressure = 0

                    allResults[count].append(pressure)
                    count = count + 1

                    listofnodes.append(nodeCode)
                    listofnodepressure.append(pressure)
                    if i == 0:
                        basecodes.append(nodeCode)
                        basepressures.append(pressure)
        
        for iRec in range(valves.RecordCount()):
            if valves.IsRecordAlive(iRec):
                valves.SetText(fldOpen, iRec, "OPEN")  
                if random.randint(0,1) == 0:
                    valves.SetText(fldOpen, iRec, "CLOSED")                    

    progbar.Close()

    with open("D:\Work\Temp.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        for iData in allResults:
            writer.writerow(iData)

    list_of_tuples = list(zip(listofnodes, listofnodepressure))
    plt.plot()
    df = pd.DataFrame(list_of_tuples, columns = ['Code', 'Pressure'])   
    ax = sns.boxplot(x="Code", y="Pressure", data=df)

    list_of_tuples = list(zip(basecodes, basepressures))
    df = pd.DataFrame(list_of_tuples, columns = ['Code', 'Pressure'])       
    ax = sns.pointplot(x="Code", y="Pressure", data=df)

    plt.show()

if __name__ == "__main__":
    TestRoutine1()  