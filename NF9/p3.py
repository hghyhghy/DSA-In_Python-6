

# to find the sum of all items in a dictionary 

# creating a function 

def ofsum(dict1):

    res=[]

    for i in dict1:

        res.append(dict1[i])

    tot=sum(res)

    return tot

dict1={'a':100,"b":200,"c":300}

print(ofsum(dict1))

# approach 2

def ofsum1(d1):

    # creating an empty variable 

    sum=0

    for i in d1.values():

        sum+=i

    return sum

d1={'a':100,"b":200,"c":300}


print(ofsum1(d1))