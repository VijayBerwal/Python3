
from sys import argv 

script , filename = argv
again = 'y'
txt = open(filename) #open a file and assign the handle(file object) to the varialble (txt) 
txt.close()	
bi =open(filename,"rb")

print("Here is your file %r : " %bi)

print("Here is your file %r : " %filename)

#print (txt.read()) #methods can be called on handle.

while again=='y' :
     again=input("Do you want to open another file(y/n)?" )
     if again == 'y':
         filename=input("Please enter the file name :" )
         txt = open(filename)
         print ("Below is the file content :::::")
         print(txt.read())
     print("End of printing files")

txt.close()	 