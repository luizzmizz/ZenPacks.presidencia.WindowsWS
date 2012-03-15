from subprocess import PIPE,Popen
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import os
import binascii

class OSMonitorMap(PythonPlugin):
    maptype = "OSComponentMap" 
    modname = "ZenPacks.presidencia.WindowsWS.HWScreen"
    relname = "hwscreen"
    compname= "hw"

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
            log.debug('EDID:%s'%Edid)
            log.debug('ProductKey:%s'%ProductKey)
            [SerialNumber,Model]=self.decodeEdid(Edid,log)
            values.append([SerialNumber,Model,ProductKey])
        return values 

    def process(self, device, results, log):
        log.info('Collecting monitor info from regshell on //%s' % device.id)
        rm = self.relMap()
        log.info('Results: %s'%results)
        if results:
          for mon in results :
              om = self.objectMap()
              om.id=om.sn=mon[0]
              om.model=mon[1]
              om._prodKey=mon[2]
              om.setProduct = MultiArgs(om._prodKey, 'Unknown Monitors')
              om.setProductKey = om._prodKey
              log.debug('_prodKey:%s'%(om._prodKey))
              rm.append(om)
        log.error('RelationMap: %s'%rm)
        return rm

    def decodeEdid(self,edid,log):
        hEdid=binascii.unhexlify(edid)
        vedid=[ ord (val) for val in hEdid ]
        sn=((vedid[15]<<24)+(vedid[14]<<16)+(vedid[13]<<8)+(vedid[12]))
        log.debug('SN:%s'%sn)
        if sn==0x01010101:
	  sn=hEdid[113:125].split('\n')[0].strip()
        else:
	  sn=str(sn)
        log.debug('SN:%s'%sn)
        model=hEdid[95:108].split('\n')[0].strip()
        log.debug('MODEL:%s'%model)
        return [sn,model]
