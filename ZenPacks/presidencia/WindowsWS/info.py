################################################################################
#
# This program is part of the RDBMS Zenpack for Zenoss.
# Copyright (C) 2009, 2010 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of Databases.

$Id: info.py,v 1.3 2010/09/28 16:18:47 egor Exp $"""

__version__ = "$Revision: 1.3 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.presidencia.WindowsWS import interfaces

 
class HWScreenInfo(ComponentInfo):
   implements(interfaces.IHWScreenInfo)
   
   type = ProxyProperty("type")
   model = ProxyProperty("model")
   sn = ProxyProperty("sn")
   tag = ProxyProperty("tag")
   serialNumber = ProxyProperty("serialNumber")
   #asciisn = ProxyProperty("asciisn")
   #activeTime = ProxyProperty("activeTime")
   @property
   def getManufacturer(self):
     return self._object.getManufacturerLink()
   @property
   def getProductKey(self):
     return self._object.getProductLink().replace(self._object.productClass().name,self._object.productClass().getProductKey())
   @property
   def getProductName(self):
     return self._object.getProductLink()
   @property
   def getDescription(self):
     return self._object.getDescription()


class LocalPrinterInfo(ComponentInfo):
    implements(interfaces.ILocalPrinterInfo)
    
    caption = ProxyProperty("caption")
    localPrinterName = ProxyProperty("localPrinterName")
    resx = ProxyProperty("resx")
    resy = ProxyProperty("resy")
    portName = ProxyProperty("portName")
    driverName = ProxyProperty("driverName")
    local = ProxyProperty("local")
    @property
    def isDefault(self):
      return self._object.isDefault()

class WindowsProfileInfo(ComponentInfo):
    implements(interfaces.IWindowsProfileInfo)
    
    path = ProxyProperty("path")
    lastUsed = ProxyProperty("lastUsed")
    profileSize = ProxyProperty("profileSize")
    
    @property
    def active(self):
      return self._object.active()
    @property
    def getProfileSize(self):
      return self._object.getProfileSize()
    @property
    def getDesktopSize(self):
      return self._object.getDesktopSize()
