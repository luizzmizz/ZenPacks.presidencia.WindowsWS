__doc__="""ProductMap
"""
__version__ = '$Revision: 1.8 $'[11:-2]

from ZenPacks.community.WMIDataSource.WMIPlugin import WMIPlugin
from Products.DataCollector.plugins.DataMaps import MultiArgs
from DateTime import DateTime

class HRSWInstalledMap(WMIPlugin):

    maptype = "SoftwareMap"
    modname = "Products.ZenModel.Software"
    relname = "software"
    compname = "os"

    tables = {
        "Win32Reg_AddRemovePrograms": (
            "Win32Reg_AddRemovePrograms",
            None,
            "root/cimv2",
            {
                'DisplayName':'setProductKey',
                'InstallDate':'setInstallDate',
                'Publisher':'_vendor',
#                'Version':'version',
            }
        ),
        "Win32_QuickFixEngineering": (
            "Win32_QuickFixEngineering",
            None,
            "root/cimv2",
            {
                'HotFixID':'setProductKey',
                'InstalledOn':'setInstallDate',
                'Description':'_vendor',
            }
        ),
    }


    def process(self, device, results, log):
        """collect WMI information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        rm = self.relMap()
        for instance in results.get("Win32Reg_AddRemovePrograms", []):
            try:
              instance['setInstallDate']=DateTime(instance['setInstallDate']).strftime('%Y/%m/%d')
            except:
              instance['setInstallDate']='1980/01/01'
              pass
            match=[om for om in rm if om.id==instance['setProductKey']]
            if not match: 
              try:
                  om = self.objectMap(instance)
                  if not om.setProductKey: continue
                  om.id = self.prepId(om.setProductKey)
                  if not om._vendor: om._vendor = 'Unknown'
                  om.setProductKey = MultiArgs(om.setProductKey, om._vendor)
                  rm.append(om)
              except AttributeError:
                  continue
            else:
              log.debug('Duplicate: %s'%instance['setProductKey'])

        for instance in results.get("Win32_QuickFixEngineering", []):
            try:
              instance['setInstallDate']=DateTime(instance['setInstallDate']).strftime('%Y/%m/%d')
            except:
              instance['setInstallDate']='1980/01/01'
              pass
            match=[om for om in rm if om.id==instance['setProductKey']]
            if not match: 
              try:
                  om = self.objectMap(instance)
                  om._vendor='Microsoft' 
                  if not om.setProductKey: continue
                  om.id = self.prepId(om.setProductKey)
                  om.setProductKey = MultiArgs(om.setProductKey, om._vendor)
                  rm.append(om)
              except AttributeError:
                  continue
            else:
              log.debug('Duplicate: %s'%instance['setProductKey'])

        return rm
