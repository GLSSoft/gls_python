import GLS

general = GLS.General

def __init__(self):
  self.FLayer = 0

def CommandLine(iFunction):
  general.CommandLine(iFunction)

def ShowNotification(message,index):
  """
        // Windows Message
      {0}ntShowMsg,
      {1}ntShowSuccessMsg,
      {2}ntShowActionMsg,
      {3}ntShowErrorMsg,
      // Windows Dialogs
      {4}ntMsgDialog_YesNo,
      {5}ntMsgDialog_YesNoCancel,
      {6}ntMsgDialog_YesAllNoAllCancel,
      {7}ntMsgDialog_OKCancel,
      {8}ntMsgDialog_AbortRetryIgnore,
      {9}ntMsgDialog_AbortIgnore,
      // Console only outputs
      {10}ntSuccess,
      {11}ntWarning,
      {12}ntError,
      {13}ntDefault,
      {14}ntSubtle,
      {15}ntBenchmark,
      {16}ntPerformanceCounter,
      {17}ntNoLogging,
      {18}ntErrorWithMessage,
      // Subtle dialogs
      {19}ntBoxWithConsoleTop_Error,
      {20}ntBoxWithConsoleTop_Action,
      {21}ntBoxWithConsoleTop_Success,
      {22}ntBoxWithConsoleBottom_Error,
      {23}ntBoxWithConsoleBottom_Action,
      {24}ntBoxWithConsoleBottom_Success,
      {25}ntBoxOnlyConsoleTop_Error,
      {26}ntBoxOnlyConsoleTop_Action,
      {27}ntBoxOnlyConsoleTop_Success,
      {28}ntBoxOnlyConsoleBottom_Error,
      {29}ntBoxOnlyConsoleBottom_Action,
      {30}ntBoxOnlyConsoleBottom_Success,
      {31}ntOptionsList,
      {32}ntOptionsButtons,
      {33}ntOptionsButtonsOnRight,
      {34}ntShowURL
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
  