# python program to \print uncommon words from two string 

def uncommon(A,B):


    # splitting the strings 


    A=A.split()

    B=B.split()

    # creating an empty list 

    x=[]

    # using a for loop 
    

    for i in A:

        if i not in B:

            x.append(i)

    for y in B:

        if y not in A:

            x.append(y)

    x=list(set(x))

    return x

A="I am Subham Sarkar"

B="My name is Subham Sarkar"

print(uncommon(A,B))




        



     