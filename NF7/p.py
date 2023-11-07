# importing namedtuple 

from collections import namedtuple

# initializing the named tuple 


students=namedtuple('student',['name','age','DOB'])

s=students('Subham','20','9102003')


print("The name of the student is ")

print(s.name)

print("The age of the student is  ")

print(s.age)

print("The DOB of the student is ")

print(s.DOB)

# printing all the fields 

print("The name of the fields of the namedtuple is ")

print(s._fields)



