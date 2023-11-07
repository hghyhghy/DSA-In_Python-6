

# importing namedtuple 


from collections import namedtuple

# initializing it 

students=namedtuple('student',['name','age','DOB'])

s=students('Shreyoshi','19','1352004')

print("The name of the student is ")

print(s.name)

print("The age  of the student is ")

print(s.age)

print("The DOB of the student is ")

print(s.DOB)

# renaming the values 

print("After renaming the namedtuple becomes ")

print(students.__new__(students,'Himesh','20','20102003'))

