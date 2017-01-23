import random
import sys
import os

#Prints out "Hello World".
print("Hello World.")

name = "Clint"

print(name)

# Numbers, Strings, Tuples, characters,
quote = "\"Always remember the backslash\""
multi_line_quote = ''' Does this work?
I do not know...
'''


#Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', '7']
print('The first item is: ', grocery_list[0])
print(grocery_list[0:3])

other_events = ['Wash Car' , 'Pick up Kids']
grocery_list.sort()
list_of_lists = [other_events, grocery_list]
super_villains = {'Fiddler' : 'Issac Bowin' , 'Superman' : 'Kurt'}
print(super_villains['Superman'])

#Conditionals if else
age = 21
if age>16 :
    print('You are old enough to drive')
elif age>=21:
    print('f')
else :
    print('Sorry')

if((age >=1) and (age <=18)) :
    print('You get a birthday')
elif (age ==21) or (age==40):
    print('You get a bday')
elif(not(age == 25)) :
    print(age)

n=5
while n > 0:
	print n
	n = n-1
print "Blastoff!"	
	
	
print(list_of_lists[1][1])

del grocery_list[2]

#Tuples can't be changed
pi_tuple = (3,1,4,2,5,9)


#Dictionaries

#