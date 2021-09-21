from bokeh.models.sources import ColumnDataSource
from bokeh.models.tools import HoverTool
import gls_python.wadiso as data
import gls_python.general as general
from bokeh.plotting import figure, save
from bokeh.models import LinearColorMapper
from bokeh.palettes import Category10

p = figure(title="Interactive Model")

def RenderNodes():
    global p

    model = data.Model()
    table = model.NodeTable()

    fldGeom = table.FieldIndex("Geometry")
    if fldGeom == -1:
        return

    fldCode = table.FieldIndex("Node_Code")
    if fldCode == -1:
        return

    fldDemands = table.FieldIndex("Demand_Scenario1")
    if fldDemands == -1:
        return

    x_coords = []
    y_coords = []
    codes = []
    demands = []

    progBar = general.ProgressBar("Adding points...", table.RecordCount())

    for iRec in range(table.RecordCount()):
        x,y = table.GetPoint(fldGeom, iRec).xy  
        x_coords.append(x[0])
        y_coords.append(y[0])

        codes.append(table.GetText(fldCode,iRec))
        demands.append(table.GetDouble(fldDemands,iRec))

        progBar.Increment()

    progBar.Close()

    dataset = dict(
        x=x_coords,
        y=y_coords,
        demand=demands,
        code=codes
    )

    cds = ColumnDataSource(data=dataset)

    #p.circle(x="x", y="y", source=cds, radius='demand', color="red")
    color_mapper = LinearColorMapper(palette="Turbo256", low=min(dataset["demand"]), high=max(dataset["demand"]))
    p.circle(x="x", y="y", source=cds, radius='demand', color={'field': 'demand', 'transform': color_mapper})

    

def RenderLinks():
    global p

    model = data.Model()
    table = model.PipeTable()

    fldGeom = table.FieldIndex("Geometry")
    if fldGeom == -1:
        return

    fldCode = table.FieldIndex("Link_Code")
    if fldCode == -1:
        return

    fldDiameter = table.FieldIndex("Diameter")
    if fldDiameter == -1:
        return

    x_coords = []
    y_coords = []
    codes = []
    diameters = []

    progBar = general.ProgressBar("Adding links...", table.RecordCount())

    for iRec in range(table.RecordCount()):
    #for iRec in range(10):
        coords = table.GetPolyline(fldGeom, iRec).xy
        
        x = []
        y = []

        for i in coords[0]:
            x.append(i)

        for i in coords[1]:
            y.append(i)

        x_coords.append(x)
        y_coords.append(y)

        codes.append(table.GetText(fldCode,iRec))
        diameters.append(table.GetDouble(fldDiameter,iRec)*0.01)

        progBar.Increment()

    progBar.Close()

    dataset = dict(
        x=x_coords,
        y=y_coords,
        diameter=diameters,
        code=codes
    )

    cds = ColumnDataSource(data=dataset)

    color_mapper = LinearColorMapper(palette=Category10[10], low=min(dataset["diameter"]), high=max(dataset["diameter"]))
    print(min(dataset["diameter"]))
    print(max(dataset["diameter"]))
    p.multi_line("x", "y", source=cds, color={'field': 'diameter', 'transform': color_mapper}, line_width="diameter")


def SaveFile():
    global p

    tooltips = [("(x,y)","($x,$y)")]
    p.add_tools(HoverTool(tooltips=tooltips))

    p.plot_height=800
    p.plot_width=1024

    outfp = r"C:\Users\adrian\Desktop\GLS\Demo\model.html"
    general.ShowNotification("Saving to " + outfp,14)
    save(obj=p, filename=outfp)  

if __name__ == "__main__":
    RenderNodes() 
    RenderLinks() 
    SaveFile() 

    general.ShowNotification("Complete",1)  