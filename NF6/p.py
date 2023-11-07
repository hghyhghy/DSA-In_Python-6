from collections import namedtuple

# importing named tuple 

# declaring namedtuple 

student=namedtuple('student',['name','age','DOB'])

#ddding values to the namedtuple 

s=student('shreyoshi','19','24102004')

print("The student at the age index", end=" " )

print(s[1])

print("The name of the student using keyname is ")

print(s.name)

