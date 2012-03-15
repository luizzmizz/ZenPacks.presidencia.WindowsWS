__doc__="""OSMonitor

OSMonitor is a Operating System Monitor (Screen)

"""

__version__ = "$Revision: 1.5 $"[11:-2]

from Globals import InitializeClass, DTMLFile
from AccessControl import ClassSecurityInfo
from Products.ZenModel.HWComponent import HWComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ZenossSecurity import *
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.ZenRelations.RelSchema import *

import binascii

class HWScreen(HWComponent):
    """
    HWScreen object
    """

    ZENPACKID = 'ZenPacks.presidencia.WindowsWS'

    portal_type = meta_type = 'HWScreen'


    #sn:        serialNumber@HWComponent
    #model:     tag@HWComponent

    _relations = HWComponent._relations + (
        ("hw", ToOne(ToManyCont, "Products.ZenModel.DeviceHW", "hwscreen")),
        )

    security = ClassSecurityInfo()

    security.declareProtected(ZEN_VIEW, 'getParentLastLogon')
    def getParentLastLogon(self):
        return self.getParentNode().getParentNode().getHWTag()

    def setModelName(self,productName,productKey,manufacturer="Unknown Monitors"):
      if self.getDmd().Manufacturers.findProduct(productKey):
        self.setProductKey(productKey,manufacturer)
      else:
        self.setProduct(productName,manufacturer)
        pks=[ pk for pk in self.productClass().productKeys if pk<>productName ]
        if productKey not in pks:
          pks.append(productKey)
        self.productClass().productKeys=pks


InitializeClass(HWScreen)
