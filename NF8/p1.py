# python program to print even length words 

# creating a string first 

s="Hello My name is Subham Sarkar "

# splitting the string 

n=s.split(" ")

# using a for loop 

for i in n:

    if len(i)%2==0:

        print(i)

# by using function 

def ofeven(s):

    n=s.split(" ")

    for i in n:

        if len(i)%2==0:

            print(i)


s="Hey How are You My Dear"

ofeven(s)

# method using list comprehension 

string="I am the hero of my life"

n=string.split(" ")

print([x for x in n if len(x)%2==0])