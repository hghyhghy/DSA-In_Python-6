
# find the words which are greater than a given length ofk k 

# creating a function 

def oflength(k,string):

    # creating an empty  string 

    string1=[]

    text=string.split(" ")

    for x in text:

        if len(x) > k:

            string1.append(x)

    return string1


k=3

string="I am Subham Sarkar"

print(oflength(k,string))