from turtle import color
from tqdm import tqdm
from wadiso import Model as activemodel
import matplotlib.pyplot as plt
from abgis import AlbionGisLayer as AbGIS
import matplotlib.colors

from tqdm import tqdm

def TestRoutine1():
    
    nodeTable = activemodel.NodeTable()
    pipeTable = activemodel.PipeTable()
    
    nodeFldOutput = nodeTable.FieldIndex("Output")
    pipeFldFlow = pipeTable.FieldIndex("Flow")    
    pipeFldOpen = pipeTable.FieldIndex("Pipe_Status")
    
    nodeTable.Lock() #required to edit the model
    nodeTable.SetDouble(nodeFldOutput, 5, 200)     
    
    pipeTable.SetText(pipeFldOpen, 3, "OPEN")  #OPEN #CLOSED   
    
    AbGIS.CommandLine("Wadiso.BalanceModel")    
        
    nodeResultOutput = nodeTable.GetDoubleAll(nodeFldOutput)
    pipeResultFlow   = pipeTable.GetDoubleAll(pipeFldFlow)    
    
    cmap = plt.cm.rainbow
    norm = matplotlib.colors.Normalize(vmin=0, vmax=20)    
    
    nodeGeom = nodeTable.GetPointAll()
    buffer = nodeGeom.buffer(200, cap_style = 3)
    for i in tqdm(range(len(buffer))):
        x,y =  buffer[i].exterior.xy 
        plt.plot(x,y,color=cmap(norm(nodeResultOutput[i]))) 
    
    norm = matplotlib.colors.Normalize(vmin=0, vmax=200)
    
    pipeGeom = pipeTable.GetPolylineAll()
    buffer = pipeGeom.buffer(20)
    for i in tqdm(range(len(buffer))):
        x,y =  buffer[i].exterior.xy   
        plt.plot(x,y,color=cmap(norm(pipeResultFlow[i]))) 

    # Add title
    plt.title("WGS84 projection")

    # Remove empty white space around the plot
    plt.tight_layout()  
    plt.savefig("C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\image.png")
    plt.show()

if __name__ == "__main__":
    TestRoutine1()  