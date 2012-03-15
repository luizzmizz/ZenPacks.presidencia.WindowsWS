__doc__="""Last Logon Map
"""

from ZenPacks.community.WMIDataSource.WMIPlugin import WMIPlugin

class LastLogonMap(WMIPlugin):
    """
    Record basic hardware/software information based on the Win32_ComputerSystem
    and Win32_OperatingSystem.
    """

    maptype = "LastLogonMap" 

    tables = {
        "Win32_ComputerSystem": (
            "Win32_ComputerSystem",
            None,
            "root/cimv2",
            {
                'UserName':'lastLogon',
            },
        ),
    }


    def process(self, device, results, log):
        """collect WMI information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        try:
            cs = results.get('Win32_ComputerSystem', [None])[0]
            om = self.objectMap()
            om.setHWTag=cs['lastLogon'][::-1].split('\\')[0][::-1]
        except:
            return
        return om

