# -*- coding: utf-8 -*-
print ("I am all ears")
print ("Hellow python world!")

# I will complete this book by end of october
print ("Make your script print another line")


print ("Now i will count my friends")
print ("friends",1+1)

print ("this is just modulo operator",2%2)

print (3+3+4-1 <5)

#Excersise 2 

cars = 100
space_in_car = 4
drivers =30
car_not_driven = cars-drivers
car_driven =drivers
carpoolcapacity = car_driven*space_in_car
passengers = 90 
avg_passengers_per_car =  passengers / car_driven

print ("there are ",cars, "cars available")
print ("There are ",drivers,"drivers available")
print ("There will be ",car_not_driven," empty cars today")
print ("We can transport ",carpoolcapacity,"passengers today")
print ("we need to put about" ,avg_passengers_per_car," in each car")


print("---------------------------------------------------------------Excersise 3") 

my_name ='vijay kumar'
my_age =27
my_height =173 # cms
my_teeth ='white'
my_eyes = 'Brown'

#print ("Lets talk about "+str(my_age)+" and "+str(my_name))
#print ("My name is %s and weight is %d kg!" % ('Zara', 21) )

print ("If i add %d ,%d i would get %d , r'\\n' " %(my_age,my_height,my_age+my_height))

print ("If i add %d ,%d i would get %r , r'\\n' " %(my_age,my_height,my_age+my_height))


print("---------------------------------------------------------------Excersise 6") 

x="There are %d types of people."%10
binary = 'binary'
do_not ="don't"

y="Those who know %s and those who %s."%(binary,do_not)


print(x)
print(y) 

print ("I said: %r" %(x))
print ("I also said : '%s'"%(y))
print ("I also said : '%s"%(y))

hilarious = False
joke_evaluation ="Isnt that joke so funny?!%r"

print(joke_evaluation%hilarious)

w="This is left side of ..."
e="a string with a right side."
print (w+e)

print("---------------------------------------------------------------Excersise 7")


print ("Mary had a little lanb.")
print ("Its fleece was white as %s" %'snow')
print ("and everywhere that mary went")
print ("."*10) # THis will print . 10 times

end1 ='C' 
end2 ='h'
end3 ='e' 
end4 ='e'
end5 ='s' 
end6 ='e'
end7 ='B' 
end8 ='r'
end9 ='r' 
end10 ='g'
end11 ='e' 
end12 ='r'

print(end1+end2+end3+end4+end5+end6 , # This comman marks the continuation of line 
end7+end8+end9+end10+end11+end12)


print("---------------------------------------------------------------Excersise 8")

formatter = "%s %s %s %r"
print (formatter %(1,2,3,4))
print (formatter %('one','two','three','four'))
print (formatter %(True,False,False,True))
print (formatter %(formatter,formatter,formatter,formatter))
print (formatter %('I am ok','this not','I m fine',"so i said good night"))


print("---------------------------------------------------------------Excersise 9")

days ="Mon Tues Wed thu Fri Sat Sun"
Months= "Jan \n feb\nMar\nApr\nMay\nJun\njul\nAug\nsept\noct\nnov\ndec " 

print ("here are the days: " ,days)
print ("here are the days: " ,Months)









































