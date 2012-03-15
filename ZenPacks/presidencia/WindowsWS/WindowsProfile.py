
__doc__="""OSMonitor

OSMonitor is a Operating System Monitor (Screen)

"""

__version__ = "$Revision: 1.5 $"[11:-2]

from Products.ZenModel.OSComponent import OSComponent
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.ZenRelations.RelSchema import *
from Globals import InitializeClass

import binascii

class WindowsProfile(OSComponent):
  """
  WindowsProfile Object
  """
  
  ZENPACKID = 'ZenPacks.presidencia.WindowsWS'
  
  portal_type = meta_type = 'WindowsProfile'
  
  path=""
  lastUsed=""
  special=""
  desktopBytes=0
  profileBytes=0
  
  _properties = OSComponent._properties + (
  {'id':'path', 'type':'string', 'mode':'w'},
  {'id':'lastUsed', 'type':'string', 'mode':'w'},
  {'id':'special', 'type':'boolean', 'mode':'w'},
  {'id':'desktopBytes', 'type':'number', 'mode':'w'},
  {'id':'profileBytes', 'type':'number', 'mode':'w'},
  )
  
  _relations = OSComponent._relations + (
  ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "windowsprofile")),
  )

  def active(self):
    if self.device().getHWTag()==self.id.split('.')[0]:
      return 'clear' 
    else:
      return 'debug'

  def getProfileSize(self):
    """
    Return the number of total bytes
    """
    return convToUnits(self.profileBytes, divby=1000)

  def getDesktopSize(self):
    """
    Return the number of total bytes
    """
    return convToUnits(self.desktopBytes, divby=1000)

InitializeClass(WindowsProfile)
