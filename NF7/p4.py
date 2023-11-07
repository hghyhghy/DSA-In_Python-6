

# operation on heap

import heapq


# creating a list 

li=[1,3,2,4,7,5,8,6]

heapq.heapify(li)

print("The newly created heap is ")

print(list(li))

print("After pushing new element to the heap it becomes ")

heapq.heappush(li,99)

print(li)

# heappop() used to pop all element and return the least element


print("The poppped and the smallest element is ")

print(heapq.heappop(li))

