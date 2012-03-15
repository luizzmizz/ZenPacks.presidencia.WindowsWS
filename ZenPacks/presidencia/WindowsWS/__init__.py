
import Globals
import os.path
#from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenModel.DeviceHW import DeviceHW
from Products.ZenRelations.RelSchema import *

OperatingSystem._relations += (("localprinter", ToManyCont(ToOne,
                                    "ZenPacks.presidencia.WindowsWS.LocalPrinter", "os")),
                               ("windowsprofile", ToManyCont(ToOne,
                                    "ZenPacks.presidencia.WindowsWS.WindowsProfile", "os")),
                               )

DeviceHW._relations +=(("hwscreen", ToManyCont(ToOne,
                            "ZenPacks.presidencia.WindowsWS.HWScreen", "hw")),
                            )
skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

