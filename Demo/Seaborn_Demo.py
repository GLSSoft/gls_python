import gls_python.adb as database   
import gls_python.abgis as gis
import gls_python.wadiso as data

import seaborn as sns
import pandas as pd         
import matplotlib.pyplot as plt

def TestRoutine1():
    # Get the active model
    model = data.Model()

    # Get the pipe table, this will return an AlbionDataBase
    pipes = model.PipeTable()

    # Get the diameter field index
    diameterField = pipes.FieldIndex('Diameter')
    fldLength = pipes.FieldIndex('Length')

    # Create lists
    listOfDiameters = []
    lengths = []

    for i in range(pipes.RecordCount()):
        listOfDiameters.append(pipes.GetDouble(diameterField,i)) 
        lengths.append(pipes.GetDouble(fldLength,i))

    list_of_tuples = list(zip(listOfDiameters, lengths))

    df = pd.DataFrame(list_of_tuples, columns = ['Size', 'Length'])   
    ax = sns.boxplot(x="Size", y="Length", data=df)
    plt.show()

if __name__ == "__main__":
    TestRoutine1()  