/*
################################################################################
#
# This program is part of the RDBMS Zenpack for Zenoss.
# Copyright (C) 2009, 2010 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.WindowsProfilePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'WindowsProfile',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'type'},
                {name: 'locking'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'path'},
                {name: 'active'},
                {name: 'activeBool'},
                {name: 'lastUsed'},
                {name: 'getProfileSize'},
                {name: 'getDesktopSize'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
		renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Profile Name'),
                sortable: true,
                width: 60
            },{
                id: 'active',
                dataIndex: 'active',
                header: _t('Last Logon'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 100
            },{
                id: 'lastUsed',
                dataIndex: 'lastUsed',
                header: _t('Last Used'),
                sortable: true,
                width: 200
            },{
                id: 'path',
                dataIndex: 'path',
                header: _t('Path'),
                sortable: true,
                width:300
            },{
                id: 'profileSize',
                dataIndex: 'getProfileSize',
                header: _t('Profile Size'),
                sortable: true,
                width:100
            },{
                id: 'desktopSize',
                dataIndex: 'getDesktopSize',
                header: _t('Desktop Size'),
                sortable: true,
                width:100
            }]
        });
        ZC.WindowsProfilePanel.superclass.constructor.call(this, config);
    }
});
ZC.HWScreenPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HWScreen',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'getProductName'},
                {name: 'getManufacturer'},
                {name: 'getProductKey'},
                {name: 'getDescription'},
                {name: 'name'},
                {name: 'type'},
                {name: 'locking'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Serial Number'),
                sortable: true
            },{
                id: 'getProductName',
                dataIndex: 'getProductName',
                header: _t('Model Name'),
                sortable: true,
                width: 200
            },{
                id: 'getManufacturer',
                dataIndex: 'getManufacturer',
                header: _t('Manufacturer'),
                sortable: true,
                width: 100
            },{
                id: 'getProductKey',
                dataIndex: 'getProductKey',
                header: _t('Product Key'),
                sortable: true,
                width: 100
            },{
                id: 'getDescription',
                dataIndex: 'getDescription',
                header: _t('Description'),
                sortable: true,
                width: 300
            }]
        });
        ZC.HWScreenPanel.superclass.constructor.call(this, config);
    }
});
  
ZC.LocalPrinterPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'LocalPrinter',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'caption'},
                {name: 'driverName'},
                {name: 'local'},
                {name: 'isDefault'},
//                 {name: 'resx'},
//                 {name: 'resy'},
                {name: 'portName'},
                {name: 'name'},
                {name: 'type'},
                {name: 'locking'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'caption',
                header: _t('Name'),
                sortable: true,
		width: 70
            },{
                id: 'portName',
                dataIndex: 'portName',
                header: _t('Port Name'),
                sortable: true,
                width: 250
            },{
                id: 'driverName',
                dataIndex: 'driverName',
                header: _t('Driver'),
                sortable: true,
                width: 250
            },{
                id: 'local',
                dataIndex: 'local',
                header: _t('Local'),
                sortable: true,
                width: 80
             },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 60
            }]
        });
        ZC.LocalPrinterPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('HWScreenPanel', ZC.HWScreenPanel);
ZC.registerName('HWScreen', _t('Monitor'), _t('Monitors'));
Ext.reg('LocalPrinterPanel', ZC.LocalPrinterPanel);
ZC.registerName('LocalPrinter', _t('Printer'), _t('Printers'));
Ext.reg('WindowsProfilePanel', ZC.WindowsProfilePanel);
ZC.registerName('WindowsProfile', _t('User Profile'), _t('User Profiles'));
})();
