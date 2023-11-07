import collections

student=collections.namedtuple('student',['name','age','DOB'])

s=student('Subham','20','9102003')

print("The name of the student is ")

print(s.name)

print("The age of the student is ")

print(s.age)

print("The DOB of the student is  ")

print(s.DOB)

# making another list to namedtuple

li=['Manjeet','19','2341999']

print("The new list to the namedtuple is ")

print(student._make(li))