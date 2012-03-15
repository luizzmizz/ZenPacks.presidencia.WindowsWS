from ZenPacks.community.WMIDataSource.WMIPlugin import WMIPlugin
import os

class WindowsProfileMap(WMIPlugin):

  maptype = "WindowsProfileMap"
  compname = "os"
  relname = "windowsprofile"
  modname = "ZenPacks.presidencia.WindowsWS.WindowsProfile"

  tables = {
    "Win32_UserProfile": (
      "Win32_UserProfile",
      {'Special':'False'},
      "root/cimv2",
        {
        'LocalPath':'path',
        'Loaded':'loaded',
        'LastUseTime':'lastUsed'
        }
    )
   }

  def process(self, device, results, log):
        """collect WMI information from this device"""
        log.info('Processing %s for device %s', self.name(), device.id)
        rm = self.relMap()
        for instance in results.get("Win32_UserProfile", []):
          try:
            instance['desktopBytes']=0
            instance['profileBytes']=0
            om = self.objectMap(instance)
            om.id = om.name = self.prepId(om.path[::-1].split('\\')[0][::-1])
            om.lastUsed = str (om.lastUsed)
            (om.profileBytes,om.desktopBytes)=self.getProfileSizes(device,log,om.path)
            rm.append(om)
          except AttributeError:
            continue
        return rm

  def getProfileSizes(self,device,log,profilePath):
    crida = 'sh %s/../../../../libexec/getProfileSize.sh %s %s %s "%s" 2>/dev/null'%(os.path.dirname(__file__),device.manageIp,device.zWinUser,device.zWinPassword,profilePath)
    f=os.popen(crida)
    for i in f.readlines():
      (profile,desktop)=(i.split(' ')[0].split(':')[1],i.split(' ')[1].split(':')[1])
    return (profile,desktop)