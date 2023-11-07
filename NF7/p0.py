
# importing the namedtuple 

from collections import namedtuple

# initializing the namedtuple 

students=namedtuple('student',['name','age','DOB'])

s=students('Shreyoshi','19','1352004')

print("The name of the student is ")

print(s.name)

print("The age  of the student is ")

print(s.age)

print("The DOB of the student is ")

print(s.DOB)

# replacing the name 

print("After replacing the name it becomes ")

print(s._replace(name='Subham'))

print(s._replace(age='20'))


 



