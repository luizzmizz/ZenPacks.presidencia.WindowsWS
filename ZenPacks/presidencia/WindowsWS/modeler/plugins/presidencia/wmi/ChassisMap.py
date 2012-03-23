__doc__="""Chassis Map
"""

from ZenPacks.community.WMIDataSource.WMIPlugin import WMIPlugin

class ChassisMap(WMIPlugin):
    """
    Record Chassis Type from Win32_SystemEnclosure
    """
    chTypes =     {1:'Other',
                   2:'Unknown',
                   3:'Desktop',
                   4:'Low Profile Desktop',
                   5:'Pizza Box',
                   6:'Mini Tower',
                   7:'Tower',
                   8:'Portable',
                   9:'Laptop',
                   10:'Notebook',
                   11:'Hand Held',
                   12:'Docking Station',
                   13:'All in One',
                   14:'Sub Notebook',
                   15:'Space-Saving',
                   16:'Lunch Box',
                   17:'Main System Chassis',
                   18:'Expansion Chassis',
                   19:'Sub Chassis',
                   20:'Bus Expansion Chassis',
                   21:'Peripheral Chassis',
                   22:'Storage Chassis',
                   23:'Rack Mount Chassis',
                   24:'Sealed-Case PC',
                   }
                   
    maptype = "ChassisMap" 

    tables = {
        "Win32_SystemEnclosure": (
            "Win32_SystemEnclosure",
            None,
            "root/cimv2",
            {
                'ChassisTypes':'cType',
            },
        ),
    }


    def process(self, device, results, log):
        """collect WMI information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        try:
            cs = results.get('Win32_SystemEnclosure', [None])[0]
            om = self.objectMap()
            om.rackSlot=self.chTypes[cs['cType'][0]]
        except Exception,e:
            log.error('Exception: %s.'%e)
            return
        return om

