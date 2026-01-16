import heapq

ls = [4, 2, 5, 1, 9]

# convert to a min-heap
first_heap = heapq.heapify(ls)
print("Heapify: ", ls)
