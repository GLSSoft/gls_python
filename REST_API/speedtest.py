from platform import node
from tracemalloc import start
from tqdm import tqdm
from wadiso import Model as activemodel

from tqdm import tqdm
import time

def TestSingleGetSetDouble():
    # total time: 550.08 for 14822 nodes
    
    startTime = time.time()
    
    nodeTable = activemodel.NodeTable()    
    nodeFldOutput = nodeTable.FieldIndex("Output")    
    record_count = nodeTable.RecordCount()
    
    # 14822 at 68.15 it/s
    outputs = []
    for i in tqdm(range(record_count)):
        outputs.append(nodeTable.GetDouble(nodeFldOutput,i))
        
    
    # 14822 at 69.06 it/s
    for i in tqdm(range(len(outputs))):
        nodeTable.SetDouble(nodeFldOutput,i,outputs[i]*1.1)
    
    #get = 3:37
    #set = 3:34
    #total time = 7:11
    
    print(str(time.time() - startTime)) 
    
def TestMulitGetSetDouble():     
    # total time: 0.22 for 14822 nodes
    # total time: 0.20 for 14822 nodes
    
    startTime = time.time()
    
    nodeTable = activemodel.NodeTable()    
    nodeFldOutput = nodeTable.FieldIndex("Output")    

    nodeOutputs = nodeTable.GetDoubleAll(nodeFldOutput)
    for i in tqdm(range(len(nodeOutputs))):
        nodeOutputs[i] = nodeOutputs[i]*1.1
    nodeTable.SetDoubleArray(nodeFldOutput,nodeOutputs)
    
    print(str(time.time() - startTime))  
    
    
if __name__ == "__main__":
    TestMulitGetSetDouble()  
    TestSingleGetSetDouble()  