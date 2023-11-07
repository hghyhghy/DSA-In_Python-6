
import heapq

# creating a list first 

li=[3,5,4,7,6,9]

print("The newly created list is ")

print(li)

# making it heap

heapq.heapify(li)

print("The newly created heap is ")

print(list(li))

print("The largest number from the heap is ")

print(heapq.nlargest(3,li))

print("The smallest number from the heap is ")

print(heapq.nsmallest(3,li))

 
