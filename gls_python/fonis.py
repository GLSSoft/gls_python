import GLS

model = GLS.Model

class Model:

  def __init__(self):
    self.FLayer = 0

  def BeginModelEvent(self):
    return model.BeginModelEvent()

  def EndModelEvent(self):
    return model.EndModelEvent()

  def NodeTable(self):
    return model.NodeTable()

  def LinkTable(self):
    return model.LinkTable()
    
  def AppurtenanceTable(self):
    return model.AppurtenanceTable()
  