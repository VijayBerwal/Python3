from sys import argv 

script , fileName = argv 

def print_all(f):
      print(f.read())
def print_a_line(LN , f):
      rewind(f,LN)
      print(f.readline(LN))
def rewind(f ,LN=0):
      f.seek(LN)

fo = open(fileName,"r")

print("the content of file %s is"%fileName)
print_all(fo)

# print("lets point file object to starting of the file")
# rewind(fo)

print("lets print 2nd line from the file")
print_a_line(13,fo)

fo.close()

