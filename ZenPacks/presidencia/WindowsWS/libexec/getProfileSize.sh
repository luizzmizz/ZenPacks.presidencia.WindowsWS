#!/bin/bash
COMPUTER=$1
USERNAME=$2
PASSWORD=$3
PROFILEPATH=$4

unitat=`echo $PROFILEPATH|awk -F ":" '{print $1}'`
path=`echo $PROFILEPATH|awk -F ":" '{print $2}'`

if  ! smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="cd \"$path\"" 2>/dev/null |grep -q "OBJECT_NAME_NOT_FOUND" ;then
  echo "Profile Path exists: calculating..." 
  profileSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;cd \"$path\";du" 2>/dev/null|grep "Total number of bytes:"|awk -F ": " '{print $2}'`
else 
  profileSize=-1
fi

if  ! smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="cd \"$path\"/Desktop" 2>/dev/null |grep -q "OBJECT_NAME_NOT_FOUND" ;then 
  echo "Profile Desktop exists:calculating...."
  desktopSize=`smbclient //$COMPUTER/$unitat$ -U $USERNAME $PASSWORD -c="recurse;cd \"$path\"/Desktop;du" 2>/dev/null|grep "Total number of bytes:"|awk -F ": " '{print $2}'`
else 
  desktopSize=-1
fi

echo -n "profileSize:$profileSize "
echo -n "desktopSize:$desktopSize "
