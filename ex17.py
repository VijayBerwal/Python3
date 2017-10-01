from sys import argv
from os.path import exists
#takes two files as input and overwrite the target file with source file
script ,from_file,to_file = argv 

# print("cpoying content %s to %s" %(from_file,to_file))

# in_file = open(from_file)
# indata = in_file.read()

# print("in_file is %d byte long"%len(indata))

# print("If target file already exists , it will be overwriten other wise no action will be taken")
# if exists(to_file) :

    # print("opening target file in write mode")
    # outfile = open(to_file,"w")
    # outfile.write(indata)
    # outfile.close()

# in_file.close()


open(to_file,'w').write(open(from_file).read())