# -*- coding:utf-8 -*-

from sys import argv 

script , fileName = argv

print ("We are going to erase file %r and then write back to it" %fileName)
print ("If you dont want to delete press Ctrl+C , other wise hit cariage return")
input("?")

print("Opening the file...")
target = open(fileName,'r+')


print("The contenet of the file is : ")
print ("\n")
for line in target.readlines():
    print(line)

print("deleting the file content!")
target.truncate()

print("Now we going to write back to file... so key in the lines")
line1=input("line1 : ")
line2=input("line2 : ")
line3=input("line3 : ")

print("I am going to write back to file these lines")
target.writelines([line1,'\n',line3,'\n',line2,'\n'])

print("finally we close it")
target.close()

