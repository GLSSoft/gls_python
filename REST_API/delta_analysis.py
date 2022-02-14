from cProfile import label
from turtle import color
from tqdm import tqdm
from wadiso import Model as activemodel
import matplotlib.pyplot as plt
from abgis import AlbionGisLayer as AbGIS
import matplotlib.colors

from tqdm import tqdm

def render(axs, results, links, title):
    axs.set_title(title)
    cmap = plt.cm.rainbow
    norm = matplotlib.colors.Normalize(vmin=0, vmax=13)
    for i in tqdm(range(len(links))):
        x,y =  links[i].exterior.xy 
        if str(i) in results:
            value = int(results[str(i)])    
            axs.plot(x,y,color=cmap(norm(value)))  
        else:
            axs.plot(x,y,color="beige") 
                

def TestRoutine1():
    nodeTable = activemodel.NodeTable()
    pipeTable = activemodel.PipeTable()
    
    pipeFldOpen = pipeTable.FieldIndex("Pipe_Status")
    nodeFldOutput = nodeTable.FieldIndex("Output")
    
    pipeGeom = pipeTable.GetPolylineAll()    
    buffer = pipeGeom.buffer(1)
    
    range_query = "Field;Flow|5;1|25;2|50;3|75;4|100;5|125;6|150;7|175;8|200;9|225;10|250;11|300;12|99999;13"
    #range_query = "Field;Average_Head|0;1|5;2|10;3|20;4|30;5|40;6|50;7|60;8|70;9|80;10|90;11|100;12|99999;13"
    
    fig, axs = plt.subplots(2, 2) 
    
    resultsBase = activemodel.Analyse("Base", "",range_query)  
    render(axs[0,0],resultsBase,buffer,"Base")
    
    nodeTable.SetDouble(nodeFldOutput, 7, 25)    
    resultsScen1 = activemodel.Analyse("Scenario1", "Base",range_query)  
    render(axs[0,1],resultsScen1,buffer,"Scenario1")  
    
    nodeTable.SetDouble(nodeFldOutput, 10, 10)    
    pipeTable.SetText(pipeFldOpen, 13, "CLOSED")  #OPEN #CLOSED   
    resultsScen2 = activemodel.Analyse("Scenario2", "Base",range_query)  
    render(axs[1,0],resultsScen2,buffer,"Scenario2")
    
    nodeTable.SetDouble(nodeFldOutput, 5, 100)     
    pipeTable.SetText(pipeFldOpen, 3, "CLOSED")  #OPEN #CLOSED   
    resultsScen3 = activemodel.Analyse("Scenario3", "Base",range_query)  
    render(axs[1,1],resultsScen3,buffer,"Scenario3")   
            
    # Remove empty white space around the plot
    plt.tight_layout()  
    #plt.savefig("C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\image.png")
    plt.show()

if __name__ == "__main__":
    TestRoutine1()  