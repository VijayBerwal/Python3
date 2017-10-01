
# -*- coding: utf-8 -*-


print ("THis is my \f \\f eg")

print ("THis is my \v \\v eg")
print ("THis is my \b \\b eg")
"""
Below code is just an infinite loop 

while True:
    for i in ["/","-","|","\\","|"]:
	    print ("%s\r"%i)
"""


#---------------------------------------------------------------------------- Exercise 11

print ("How old are you ? " , end=" ")
age = input()
print ("How tall are you? ",end=" ")
height = input()
print ("how much you weigh ?",end=" ")
weight=input()

print ("so you are %r years old, %r tall and %r heavy" %(age,height,weight))