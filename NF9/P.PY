

# getting the size of the tuple 

import sys


# creating a tuple 



t1=("a",1,"b",2,"c",3)

t2=("Subham",1,"Shreyoshi",2,"Krihna",3)

t3=("Geeks",1,"Netify",2,"Hostinger")

print("Printing the size of the tuple ")

print("The size of the tuple is " + str(sys.getsizeof(t1)) + "Bytes")

print("The size of the tuple is " + str(sys.getsizeof(t2)) + "Bytes")

print("The size of the tuple is " + str(sys.getsizeof(t3)) + "Bytes")


# method 2 by using in built sizeof method

# creating another tuple 

t4=("a",1,"b",2,"c",3)

t5=("Subham",1,"Shreyoshi",2,"Krihna",3)

t6=("Geeks",1,"Netify",2,"Hostinger")

print("Printing the size of the tuple ")

print("The size of the tuple is " + str(t4.__sizeof__()) + "Bytes")

print("The size of the tuple is " + str(t5.__sizeof__()) + "Bytes")

print("The size of the tuple is " + str(t6.__sizeof__()) + "Bytes")








