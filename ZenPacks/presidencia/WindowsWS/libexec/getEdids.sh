#!/bin/bash
COMPUTER=$1
USERNAME=$2
PASSWORD=$3
REGSHELL=/usr/local/samba/bin/regshell
cmd="$REGSHELL -U $USERNAME --password $PASSWORD --remote=$COMPUTER"

if ping -c 1 $COMPUTER > /dev/null; then 
 for DISPLAY in `echo "predef HKEY_LOCAL_MACHINE
  ck SYSTEM
  ck CurrentControlSet
  ck Enum
  ck DISPLAY
  ls"|$cmd|grep ^K|awk '{print $2}'`;do
    for DISPLAYID in `echo "predef HKEY_LOCAL_MACHINE
        ck SYSTEM
        ck CurrentControlSet
        ck Enum
        ck DISPLAY
        ck $DISPLAY
        ls"|$cmd|grep ^K|awk '{print $2}'`;do
          EDID=`echo "predef HKEY_LOCAL_MACHINE
            ck SYSTEM
            ck CurrentControlSet
            ck Enum
            ck DISPLAY
            ck $DISPLAY
            ck $DISPLAYID
            ck Control
            ck ..
            ck \"Device Parameters\"
            print EDID"|$cmd 2>/dev/null|tail -n 1`
          echo $EDID|tail -n 1|grep -v ^New > /dev/null
          if [ $? -eq 0 ]; then
            echo $EDID,$DISPLAY
	    #SN=`echo -n $EDID|perl -lne 'print pack "H*", $_'|cut -c 31-50|head -n 2|tail -n 1`
            #MODEL=`echo -n $EDID|perl -lne 'print pack "H*", $_'|cut -c 12-27|head -n 2|tail -n 1`
            #echo "SN:$SN;MODEL:$MODEL"
            #echo "DISPLAY:$DISPLAY;DISPLAYID:$DISPLAYID;EDID:$EDID;SN:$SN;MODEL:$MODEL";
          fi
        done;
 done;
fi
