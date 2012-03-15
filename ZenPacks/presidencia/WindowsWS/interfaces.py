from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IHWScreenInfo(IComponentInfo):
      """
      Info adapter for HWScreen component
      """
      serialNumber = schema.Text(title=u"Serial Number", readonly=False, group='Details')
      tag = schema.Text(title=u"Tag", readonly=True, group='Details')
      getProductName = schema.Text(title=u"Model Name", readonly=True, group='Details')
      getManufacturer = schema.Text(title=u"Manufacturer", readonly=True, group='Details')
      getProductKey = schema.Text(title=u"Product Key", readonly=True, group='Details')
      getDescription = schema.Text(title=u"Product Description", readonly=True, group='Details')
      

class ILocalPrinterInfo(IComponentInfo):
    """
    Info adapter for Local Printer component
    """
    caption = schema.Text(title=u"Printer Name", readonly=True, group='Details')
    driverName = schema.Text(title=u"Driver Name", readonly=True, group='Details')
    resx = schema.Text(title=u"Horizontal Resolution", readonly=True, group='Details')
    resy = schema.Text(title=u"Vertical Resolution", readonly=True, group='Details')
    portName = schema.Text(title=u"Port Name", readonly=True, group='Details')
    local = schema.Text(title=u"Local", readonly=True, group='Details')
    #default = schema.Text(title=u"Default", readonly=True, group='Details')

class IWindowsProfileInfo(IComponentInfo):
    """
    Info adapter for Windows Profile component
    """
    path = schema.Text(title=u"Path", readonly=True, group='Details')
    active = schema.Text(title=u"Last Logon", readonly=True, group='Details')
    lastUsed = schema.Text(title=u"Last Logon", readonly=True, group='Details')

