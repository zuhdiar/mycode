#!/usr/bin/env python3
mylist=["192.168.0.5" , 5050, "UP"]
newlist=[ 5060, "80",55,"10.0.0.1","10.20.30.1","ssh"]
print("the first item in the list is: " + mylist[0])
print("the second item in the list is: " + str(mylist[1]))
print("the last item in the list is : " + mylist[2] )

print("when i" , newlist[5] , "into IP" , newlist[3] + " or" ,  newlist[4] + " I am unable to ping ports " + str(newlist[0]) + "," + newlist[1] + "," +   "or " + str(newlist[2]) +".")
