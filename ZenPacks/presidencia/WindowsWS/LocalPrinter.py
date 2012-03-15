from Globals import InitializeClass, DTMLFile
#from AccessControl import ClassSecurityInfo
from Products.ZenModel.OSComponent import OSComponent
#from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
#from Products.ZenModel.ZenossSecurity import *
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.ZenRelations.RelSchema import *

class LocalPrinter(OSComponent):

    ZENPACKID = 'ZenPacks.presidencia.WindowsWS'

    portal_type = meta_type = 'LocalPrinter'

    caption=""
    driverName=""
    resx = 0
    resy = 0
    portName = ""
    host = ""
    local = False
    default = False

    _properties = OSComponent._properties + (
        {'id':'caption', 'type':'string', 'mode':'w'},
        {'id':'driverName', 'type':'string', 'mode':'w'},
        {'id':'name', 'type':'string', 'mode':'w'},
        {'id':'resx', 'type':'int', 'mode':'w'},
        {'id':'resy', 'type':'int', 'mode':'w'},
        {'id':'portName', 'type':'string', 'mode':'w'},
        {'id':'local', 'type':'boolean', 'mode':'w'},
        {'id':'default', 'type':'boolean', 'mode':'w'},
        {'id':'deviceId', 'type':'string', 'mode':'w'},
        )

    _relations = OSComponent._relations + (
        ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "localprinter")),
        )

    def isDefault(self):
      if self.default:
        return 'clear'
      else:
        return 'debug'

    def getParentLastLogon(self):
      return self.device().getHWTag()

InitializeClass(LocalPrinter)
