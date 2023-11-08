
# python pogram to accept the string which contains vowels 

def ofcheck(string):

    string=string.lower()

    vowels=set('aeiou')

    # creating an empty set 

    s1=set({})

    # using a for loop 

    for i in  string:

        if i in vowels:

            s1.add(i)

        else:

            pass

    if len(s1)==len(vowels):

        print("Accepted")

    else:

        print("Not Accepted")


string="aeiyuou"

ofcheck(string)