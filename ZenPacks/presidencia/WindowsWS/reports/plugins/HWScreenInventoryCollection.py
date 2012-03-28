import logging
log = logging.getLogger("zen.Reports")

from Products.ZenReports import Utils

class HWScreenInventoryCollection:
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
        components=[ c.getObject() for c in dmd.Devices.componentSearch({'meta_type':'HWScreen'}) if c.getObject().device() in resultset ]

        superreport['rackslot']=sorted(list(set([i.device().rackSlot for i in components])))
        superreport['hwman']=sorted(list(set([i.getManufacturerName() for i in components])))

        cManufacturer=args.get('cManufacturer','')
        if cManufacturer!='':
          components = [ c for c in components if c.getManufacturerName()==cManufacturer ]
          
        superreport['hwproducts']=sorted(list(set([i.getProductName() for i in components])))

        cProductName=args.get('cProductName','')
        if cProductName!='':
          components = [ c for c in components if c.getProductName()==cProductName  ]
          
        cRackSlot=args.get('cRackSlot','')
        if cRackSlot!='':
          components = [ c for c in components if c.rackSlot==cRackSlot]
        ##for each device at resultset & survivordevs, generate the info
        for c in components:
          dev=c.device()
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
                     model = c.getProductName(),
                     modelLink = c.getProductLink(),
                     productKey = c._prodKey,
                     serial = c.serialNumber,
                     manufacturerName = c.getManufacturerName(),
                     manufacturerLink = c.getManufacturerLink(),
                     rackSlot = dev.rackSlot,
                     description = c.getDescription()
                     )
                    )

        superreport['components']=report
        return superreport
