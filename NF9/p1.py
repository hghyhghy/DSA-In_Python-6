

# adding tuple to a list 

# creating a list

l=[1,2,3,4,5]

print("The original list is ")

print(l)

# creating a tuple 

test_tup=(9,10)


l+=test_tup

print("After operation the list becomes ")

print(str(l))

# by using tuple 

l1=[1,2,3,4,5]

 
print("The original list is ")

print(l1)

tup=(10,1,3)

print("The oroginal tuple is ")

print(tup)

rest=tuple(list(tup)+l1)

print("The newly created tuple is ")

print(rest)
