from subprocess import PIPE,Popen
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import os
import binascii

class HWScreenMap(PythonPlugin):
    maptype = "HWComponentMap" 
    modname = "ZenPacks.presidencia.WindowsWS.HWScreen"
    relname = "hwscreen"
    compname= "hw"
    classname= "HWScreen"

    deviceProperties = PythonPlugin.deviceProperties + (
        'zWinUser',
        'zWinPassword',
        'zWmiProxy',
    )
    
    def collect(self, device, log):
        crida = 'sh %s/../../../../libexec/getEdids.sh %s %s %s'%(os.path.dirname(__file__),device.manageIp,device.zWinUser,device.zWinPassword)
        p=Popen(crida,shell=True,stdout=PIPE,stderr=PIPE)
        stdout,stderr=p.communicate()
        values=[]
        for line in stdout.split('\n'):
          if line<>'':
            [ Edid, ProductKey ]=line.split(',')
            #edid= "".join(chr(i) for i in Edid)
            [SerialNumber,Model]=self.decodeEdid(Edid,log)
            values.append([SerialNumber,Model,ProductKey])
        return values 

    def process(self, device, results, log):
        log.info('Collecting monitor info from regshell on //%s' % device.id)
        rm = self.relMap()
        log.debug('Results: %s'%results)
        if results:
          for mon in results :
              om = self.objectMap()
              om.id=om.serialNumber=self.prepId(mon[0])
              om.tag=self.prepId(mon[1])
              om._prodKey=mon[2]
              om.setModelName=MultiArgs(mon[1],mon[2], 'Unknown Monitors')
              rm.append(om)
        return rm

    def decodeEdid(self,edid,log):
        hEdid=binascii.unhexlify(edid)
        vedid=[ ord (val) for val in hEdid ]
        sn=((vedid[15]<<24)+(vedid[14]<<16)+(vedid[13]<<8)+(vedid[12]))
        if sn==0x01010101:
	  sn=hEdid[113:125].split('\n')[0].strip()
        else:
	  sn=str(sn)
        model=hEdid[95:108].split('\n')[0].strip()
        return [sn,model]

        