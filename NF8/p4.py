

# python progrm to remove the ith character from the string 

def remove(string,i):

    A=string[: i]

    B=string[i+1 :]

    return A+B


string="subhamsarkar"

i=5

print(remove(string,i))

# method 2

def ofremove(st1,k):

    if k>len(st1):

        return st1
   
    a=list(st1)

    a.pop(k)

    return " ".join(a)



st1="subhamshreyoshisarkar"

k=4

print(ofremove(st1,k))
