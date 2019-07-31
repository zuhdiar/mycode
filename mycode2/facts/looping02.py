#!/usr/bin/env python3 
dnsfile = open("dnsservers.txt")
dnslist = dnsfile.readlines()
for x in dnslist:
    print(x, end="")
dnsfile.close()
