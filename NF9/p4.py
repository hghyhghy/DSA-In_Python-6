

# python program to remove a key from the dictionary 

# creating a dict

d={"subham":1,"Shreyoshi":2,"krishna":4,"Shatru":5}

print("The original dictionary is ")

print(d)

# using del keyword 

del d["Shatru"]

print("After deleting the key the dictionary becomes ")

print(d)

# approach 2

# by  using pop

#creating a dict

d1={"subham":1,"Shreyoshi":2,"krishna":4,"Dushman":5}

print("The original dictionary is ")

print(d1)

removed_key=d1.pop("Dushman")

print("After popping the key the dictionary  becomes ")

print(str(removed_key))



