import heapq

# creating a list 

values=[2,4,3,6,5,7]

print("The original list is ")

print(values)

# making it the heap

heapq.heapify(values)

print("The newly created heap is ")

print(list(values))

heapq.heappush(values,6)

print("After pushing the values in the heap it becomes ")

print(list(values))

smallest=heapq.heappop(values)

print("The smallest element from the heap is ")

print(smallest)

print("The nsmallest element from the list ")

nsmall=heapq.nsmallest(2,values)

print(nsmall)

print("The largest element from the heap is ")

nlarge=heapq.nlargest(2,values)

print(nlarge)