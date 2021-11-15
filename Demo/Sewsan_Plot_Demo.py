import gls_python.sewsan as sws
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import gls_python.general as general
from gls_python.general import AlbionMessageTypes as msg
from gls_python.general import ShowNotification as sn

activemodel = sws.Model()
activegravity = activemodel.GravityTable()
activestructure = activemodel.StructureTable()

plotIndividual = False

v_plot_size = [5,5]

filterQueries = [
    ["Diameter >= 100",activegravity,v_plot_size],
    ["Diameter < 100",activegravity,v_plot_size]]

saveLocation = "D:\\"

figure = 1
for vQuery in filterQueries:
    vWhere = vQuery[0]
    vTable = vQuery[1]
    vPlotSize = vQuery[2]
    vList = vTable.WhereClause(vWhere)

    if len(vList) > 0:
        plt.figure(figure)
        figure = figure + 1
        
        plt.rcParams['figure.figsize'] = vPlotSize

        y = []
        x = []
        code = []

        for vRec in vList:
            localcode = activegravity.GetText(activegravity.FieldIndex("Link_Code"),vRec)
            timestep = 0
            fldIndex = activegravity.FieldIndex("Timestep_" + str(timestep))
            while fldIndex != -1:
                y.append(activegravity.GetDouble(fldIndex,vRec))
                x.append(timestep)
                timestep = timestep + 1        
                fldIndex = activegravity.FieldIndex("Timestep_" + str(timestep))
                code.append(localcode)

        if not plotIndividual:
            data = { 'Flow': y, 'Timestep': x, 'Code': code }   
            df = pd.DataFrame(data)
            sns.lineplot(x='Timestep', y='Flow', hue='Code',data=df)
        else:
            data = { 'Flow': y, 'Timestep': x }   
            df = pd.DataFrame(data)
            sns.lineplot(x='Timestep', y='Flow',data=df)

        if saveLocation != '':
            plt.savefig(saveLocation + int(figure) + ".png")
        else:
            plt.show()
    else:    
        sn("Selection returned no results", msg.ntWarning)