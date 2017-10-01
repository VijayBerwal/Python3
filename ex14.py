
from sys import argv

script,user_name = argv  # argv[0] is always script name 
prompt = '> '  # This takes input at run time 

print ("Hi %s , I am %s script" %(user_name,script))

print ("Do you like me %s?" %user_name)
likes = input(prompt)  # input takes values from prompt

print("like me ? %s" % likes)

print ("What kind of computer you have?" )

system=input(prompt)

print("""You have %s
      and like %s"""%(system,likes))