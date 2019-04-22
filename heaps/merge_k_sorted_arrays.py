# Taken from: https://www.youtube.com/watch?v=6bvnZzwiKzs&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=35
from heap import Heap

# K number of arrays, n length of the longest array
# O(n*k)log(k)
def merge(arrays):
	inequality = lambda x,y: x[0] < y[0] 
	heap = Heap([], inequality)
	result = []
	for array in range(len(arrays)):
		heap.push((arrays[array][0], array, 0)) # Tuple: (value, array, index) 
	import pdb; pdb.set_trace()
	while heap.size() > 0:
		value, array, index = heap.pop()
		result.append(value)
		if index < len(arrays[array])-1:
			heap.push((arrays[array][index+1], array, index+1))
	return result

a1 = [1, 2, 10]
a2 = [3, 5, 8, 9, 11]
a3 = [4, 6, 7, 12]

arrays=[a1, a2, a3]

print('merge arrays:')
for array in arrays:
	print(array)
print('is: ', merge(arrays))