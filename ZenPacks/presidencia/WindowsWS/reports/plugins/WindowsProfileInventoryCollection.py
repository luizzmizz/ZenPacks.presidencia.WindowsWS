import logging
log = logging.getLogger("zen.Reports")

from Products.ZenReports import Utils

class WindowsProfileInventoryCollection:
    def run(self, dmd, args):
        report = []

        superreport={}
        #the selected devices are all the DeviceClass subdevices
        deviceClass=args.get('cDeviceClass','/')
        resultset=set(dmd.Devices.getOrganizer(deviceClass).getSubDevices())-set(dmd.Devices.getOrganizer('/Ignore').getSubDevices())
        group=args.get('cGroup','/')
        if group!='/':
          #&ed with the group specification subdevices
          resultset=resultset & set(dmd.Groups.getOrganizer(group).getSubDevices())
        system=args.get('cSystem','/')
        if system!='/':
          #&ed with the system specification subdevices
          resultset=resultset & set(dmd.Systems.getOrganizer(system).getSubDevices())
        location=args.get('cLocation','/Devices')
        if location!='/':
          #&ed with the location specification subdevices
          resultset=resultset & set(dmd.Locations.getOrganizer(location).getSubDevices())
        productionState=args.get('cProductionState','')
        if productionState!='All':
          resultset=set ([ dev for dev in resultset if dev.productionState==int(productionState) ])
        components=[ c.getObject() for c in dmd.Devices.componentSearch({'meta_type':'WindowsProfile'}) if c.getObject().device() in resultset ]
        
        superreport['profileNames']=[ c.name() for c in components ]
        
        lastLogonFilter=args.get('cLastLogonFilter','1')
        cProfileName=args.get('cProfileName','')

        
        #for each device at resultset & survivordevs, generate the info
        for c in components:
          dev=c.device()
          condition=((lastLogonFilter=='1' and (dev.getHWTag()!='' and ('\\%s'%dev.getHWTag() in c.path))) or lastLogonFilter=='0')
          condition=condition and (cProfileName=='' or (cProfileName!='' and cProfileName==c.name()))
          if condition:
            report.append(
                   Utils.Record(
                     deviceName = dev.name(),
                     deviceLink = dev.getDeviceLink(),
                     manageIp = dev.manageIp,
                     tag = dev.getHWTag(),
                     deviceClassPath = dev.getDeviceClassPath(),
                     deviceClassPathLink = dmd.Devices.getOrganizer(dev.getDeviceClassPath()).getIdLink(),
                     productionState = dev.getProdState(),
                     location = dev.getLocationName(),
                     locationLink = dev.getLocationLink(),
                     profileName = c.name(),
                     lastLogon = (dev.getHWTag()!='' and ('\\%s'%dev.getHWTag() in c.path)),
                     profileSize = c.getProfileSize(),
                     desktopSize = c.getDesktopSize(),
                     profileBytes = c.profileBytes,
                     desktopBytes = c.desktopBytes,
                     path = c.path,
                     )
                    )

        superreport['components']=report
        return superreport
