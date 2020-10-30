#!/bin/bash

# Stephen Burke - 10/30/2020 - https://github.com/se7enack

clear;echo
ping -c 3 $(ifconfig | grep broadcast | awk '{ print $2 }') > /dev/null 
arplist=$(arp -a | grep -v incomplete | awk -F " " '{ print $4 }' | grep -iv 'ff:ff:ff:ff:ff:ff' | awk -F ":" '{ print $1":"$2":"$3 }')
curl -qs `echo "aHR0cHM6Ly9naXRsYWIuY29tL3dpcmVzaGFyay93aXJlc2hhcmsvLS9yYXcvbWFzdGVyL21hbnVmCg" | base64 -D` > .vendors
for mac in ${arplist}
do
	cat .vendors | grep -i ${mac} | awk '{$2=""; print "  " $0}'
done; echo