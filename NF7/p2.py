

from collections import namedtuple

students=namedtuple('student',['name','age','DOB'])

s=students('Shreyoshi','19','1352004')

print("The name of the student is ")

print(s.name)

print("The age  of the student is ")

print(s.age)

print("The DOB of the student is ")

print(s.DOB)

# the getnewargs() func returns namedtuple as plain tuple 

print("After making the namedtuple as plain tuple it becomes  ")

print(s.__getnewargs__())
