import GLS

general = GLS.General

def __init__(self):
  self.FLayer = 0

def CommandLine(iFunction):
  general.CommandLine(iFunction)

def ShowNotification(message,index):
  print(message)
  return general.ShowNotification(message,index)

class ProgressBar:

  def __init__(self, message, count):
    self.FProgbar = general.CreateProgressBar(message, count)

  def Increment(self):
    return general.IncrementProgressBar(self.FProgbar)
    
  def Close(self):
      return general.CloseProgressBar(self.FProgbar)
  