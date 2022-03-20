
#!/usr/bin/python

# portscan.py - Stephen J. Burke / DorkCloud.com - March 10th 2016

import sys, socket, platform, os, subprocess
from optparse import OptionParser

class sbcolors:
    sbBlue = '\033[94m'
    sbGreen = '\033[92m'
    sbRed = '\033[91m'
    sbBold = '\033[1m'
    sbEnd = '\033[0m'
    
def main(myArgs):
    parser = OptionParser()
    parser.add_option("-i", help="ip address or machine name")
    parser.add_option("-p", help="port to scan")

    (options, args) = parser.parse_args()
    
    if options.i is None:
        parser.error(helper())
    i = options.i

    if options.p is None:
        parser.error(helper())
    p = options.p

    subprocess.call('clear', shell=True)

    print sbcolors.sbBlue + "..............." + sbcolors.sbEnd

    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + i + " > /dev/null"
        if os.system(hiThere) == 0:
            nowScan()
            socketCheck(i, p)
        else:
            print sbcolors.sbRed + "Bad IP or Address: "  + i + " is completely unreachable!" + sbcolors.sbEnd
    else:
        hiThere = "ping -c 1 " + i + " > /dev/null"
        if os.system(hiThere) == 0:
            nowScan()
            socketCheck(i, p)
        else:
            print sbcolors.sbRed + "Bad IP or Address: "  + i + " is completely unreachable!" + sbcolors.sbEnd

def nowScan():
    print sbcolors.sbBlue + "Now scanning..." + sbcolors.sbEnd
    print sbcolors.sbBlue + "..............." + sbcolors.sbEnd

def socketCheck(i,p):
    x = i + "," + p
    x = x.split(",")
    x[1] = int(x[1]) 
    x = tuple(x)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r = s.connect_ex(x)

    if r == 0:
        print sbcolors.sbGreen + "Up: Port " + str(p) + " is open on host " + str(i) + sbcolors.sbEnd
    else:
        print sbcolors.sbRed + "Down: Port " + str(p) + " is not open on host " + str(i) + "!" + sbcolors.sbEnd

def helper():
    print sbcolors.sbBold + ""
    print "This script scans an IP address for a particular port "
    print ""
    print ""
    print "Usage: "
    print "./portscan.py -i <ip> -p <port>"
    print ""
    print ""
    print "Example: "
    print "./portscan.py -i 192.168.1.127 -p 80"
    print ""
    print "" + sbcolors.sbEnd

if __name__ == "__main__":
    main(sys.argv[1:])
