import GLS
from enum import IntEnum

general = GLS.General

class AlbionMessageTypes(IntEnum):
      # Notifications
      ntShowMsg = 0
      ntShowSuccessMsg = 1 
      ntShowActionMsg = 2 
      ntShowErrorMsg = 3

      #Windows Dialogs
      ntMsgDialog_YesNo = 4
      ntMsgDialog_YesNoCancel = 5 
      ntMsgDialog_YesAllNoAllCancel = 6
      ntMsgDialog_OKCancel = 7
      ntMsgDialog_AbortRetryIgnore = 8
      ntMsgDialog_AbortIgnore = 9 

      #Console only outputs
      ntSuccess = 10
      ntWarning = 11
      ntError = 12
      ntDefault = 13
      ntSubtle = 14 
      ntBenchmark = 15
      ntPerformanceCounter = 16
      ntNoLogging = 17
      ntErrorWithMessage = 18 

      #Subtle dialogs
      ntBoxWithConsoleTop_Error = 19
      ntBoxWithConsoleTop_Action = 20
      ntBoxWithConsoleTop_Success = 21
      ntBoxWithConsoleBottom_Error = 22
      ntBoxWithConsoleBottom_Action = 23
      ntBoxWithConsoleBottom_Success = 24
      ntBoxOnlyConsoleTop_Error = 25
      ntBoxOnlyConsoleTop_Action = 26
      ntBoxOnlyConsoleTop_Success = 27
      ntBoxOnlyConsoleBottom_Error = 28
      ntBoxOnlyConsoleBottom_Action = 29
      ntBoxOnlyConsoleBottom_Success = 30
      ntOptionsList = 31
      ntOptionsButtons = 32
      ntOptionsButtonsOnRight = 33
      ntShowURL = 34

def CommandLine(iFunction):
  general.CommandLine(iFunction)

def ShowNotification(message,index: AlbionFieldTypes):
  """
      
  """
  print(message)
  return general.ShowNotification(message,index)

class ProgressBar:

  def __init__(self, message, count):
    """
    Ensure that the 'Close' function is called when you are finished with the progress bar
    """
    self.FProgbar = general.CreateProgressBar(message, count)

  def Increment(self):
    """
    Increments progress by 1
    """
    return general.IncrementProgressBar(self.FProgbar)
    
  def Close(self):
    """
    Call to close and destroy the progress bar
    """
    return general.CloseProgressBar(self.FProgbar)
  