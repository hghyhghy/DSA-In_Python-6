
# adding tuple to a list 

# creating a list

l=[1,3,4,5,6]

print("The original list is ")

print(l)

# by using extend method

# creating a tuple

t1=(9,10)

l.extend(list(t1))

print("after operation the  list become ")

print(str(l))

# approach 2 

l1=[2,3,4,5,6]

print("The original list is ")

print(l1)

tup=(5,6,78)

tup=list(tup)

tup.extend(l1)

tup=tuple(tup)

print("The container after operation is ")

print(str(tup))


