#!/bin/bash
COMPUTER=$1
USERNAME=$2
PASSWORD=$3
PROFILEPATH=$4

unitat=`echo $PROFILEPATH|awk -F ":" '{print $1}'`
path=`echo $PROFILEPATH|awk -F ":" '{print $2}'`

if ping -c 1 $COMPUTER > /dev/null ;then
   profileSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;du \"$path\"" 2>/dev/null|grep "Total number of bytes:"|awk -F ": " '{print $2}'`
   desktopSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;du \"$path\"/Desktop" 2>/dev/null|grep "Total number of bytes:"|awk -F ": " '{print $2}'`
   echo -n "profileSize:$profileSize "
   echo -n "desktopSize:$desktopSize "
fi
