# -*- encoding: utf-8 -*-

def print_two (*args):
    arg1,arg2=args
    print("Two args are %s %s"%(arg1,arg2))
	
def print_two_again(arg1,arg2):
    print("I got %s and %s"%(arg1,arg2))
	
print_two('a','b')
print_two_again("vijay","Kumar")