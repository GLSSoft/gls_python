import tsnet
from gls_python import general
from gls_python import wadiso

# report results
import matplotlib.pyplot as plt

def export_model(filename):    
    general.CommandLine("Wadiso.SaveToInp|"+filename)

#%%
# Open an example network and create a transient model
def setupmodel(filename):    
    tm = tsnet.network.TransientModel(filename)

    # Set wavespeed
    tm.set_wavespeed(1200.) # m/s
    # Set time options
    dt = 0.1  # time step [s], if not given, use the maximum allowed dt
    tf = 20   # simulation period [s]
    tm.set_time(tf,dt)


    # Initialize steady state simulation
    t0 = 0. # initialize the simulation at 0 [s]
    engine = 'DD' # demand driven simulator
    tm = tsnet.simulation.Initializer(tm, t0, engine)

    return tm

def addpulse(tm, code):
    # Add demand pulse
    tc = 1 # total demand period [s]
    ts = 1 # demand pulse start time [s]
    tp = 0.2 # demand pulse increase time [s]
    dp = 1 # demand pulse increase multiples [s]
    demand_pulse = [tc,ts,tp,dp]
    tm.add_demand_pulse(code,demand_pulse)    

def add_burst(tm, code):
    # Add burst
    ts = 1 # burst start time
    tc = 1 # time for burst to fully develop
    final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
    tm.add_burst(code, ts, tc, final_burst_coeff)

def analyse(tm):                                           
    # Transient simulation
    results_obj = 'Tnet1' # name of the object for saving simulation results
    return tsnet.simulation.MOCSimulator(tm, results_obj) 

def getheadatnode(tm,code):
    node = tm.get_node(code)
    return node.head

def export_to_model(tm):
    model = wadiso.Model()
    nodes = model.NodeTable()
    head = []
    model.BeginModelEvent()
    try:
        for n in tm.nodes():
            code = n[0] 
            recs = nodes.RecordsFromValue(nodes.FieldIndex("Node_Code"), code) 
            for rec in recs:   
                node = tm.get_node(code)
                if not node.head is None:
                    nodes.SetDouble(nodes.FieldIndex("Static_Head"), rec, max(node.head)) 
                    nodes.SetDouble(nodes.FieldIndex("Head"), rec, min(node.head))
    finally:
        model.EndModelEvent()

def create_plot():
    fig = plt.figure(figsize=(8,5), dpi=80, facecolor='w', edgecolor='k')

def add_simulation_to_plot(tm,head,label,linecolor):
    plt.plot(tm.simulation_timestamps,head, linecolor, label =label, linewidth=2.5)  

def save_show_and_save_plot(filename):
    #plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
    plt.xlabel("Time [s]")
    plt.ylabel("Pressure Head [m]")
    plt.legend(loc='best')
    plt.show()
    plt.savefig(filename, format='pdf',dpi=500)

if __name__ == "__main__":
    filename = "D:\\venv\\Tnet1.inp"

    #Export from wadiso
    #export_model(filename)

    create_plot()
    
    # Base analysis
    tm = setupmodel(filename)
    tm1 = analyse(tm)
    head1 = getheadatnode(tm1, 'N2')
    add_simulation_to_plot(tm1,head1,'Base','r')

    tm = setupmodel(filename)
    addpulse(tm,'N2')
    tm1 = analyse(tm)
    head1 = getheadatnode(tm1, 'N2')
    add_simulation_to_plot(tm1,head1,'Pulse','g')

    tm = setupmodel(filename)
    add_burst(tm,'N2')
    #addpulse(tm,'N2')
    tm2 = analyse(tm)
    head2 = getheadatnode(tm2, 'N2')
    add_simulation_to_plot(tm2,head2,'Burst','b')

    #write results back to wadiso
    export_to_model(tm2)

    pdffilename = 'D:/venv/demand_pulse_5.pdf'
    save_show_and_save_plot(pdffilename)