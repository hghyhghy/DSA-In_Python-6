

# python program to creaste a list of tuple from a given list having number and 

# it cube 

# creating a list first 

l=[1,3,5,7] 

print("List before operation is ")

print(l)

print("List after operation is ")

res=[(val,pow(val,3)) for val in l]

print(res)

# method 2 using ** operator 

# creating another  list 

l1=[1,2,3,4]

print("The list before operation is ")

print(l1)

print("The list before operation is ")

temp=[(val,val**3) for val in l1]

print(temp)


# method 3 by using  for loops

# creating a  list 

l2=[1,2,3,4,5]

# creating an empty list 

rest=[]

# using a for loop

for val in l2:

    tup=(val,val**3)

    rest.append(tup)


print(rest)

