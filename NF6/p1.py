

import collections


print("Using the namedruple")



student=collections.namedtuple('student',['name','age','DOB'])


# creating the object 

s=student('Subham','20','9102003')

print("The name of the student is ")


print(s.name)


print("The dateofbirth of the student ")

print(s.DOB)

print("The age of the student is  ")

print(s.age)

print("Accessing the value of the student by using getattr()")

print(getattr(s,'DOB'))


