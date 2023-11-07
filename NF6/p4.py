
import collections


student =collections.namedtuple('student',['name','age','DOB'])

# icreating the object 

s=student('subham','20','9102003')

print("The name of the student is ")

print(s.name)

print("The age of the student is ")

print(s.age)

print("The DOB  of the student is ")

print(s.DOB)

# using ** operator 

di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

print("The namedtuple instance from dict is ")


print(student(**di))
 