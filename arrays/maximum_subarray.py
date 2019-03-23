# Problem from: https://www.youtube.com/watch?v=ohHWQf1HDfU&t=33s
# Complexity: O(n^2)
def maximum_sub_array(array):
	max = float('-inf')
	start_idx = end_idx = None
	for i in range(0, len(array)):
		sum = 0
		for j in range(i, len(array)):
			sum += array[j]
			if sum > max:
				max = sum
				start_idx = i
				end_idx = j
	return max, start_idx, end_idx
print('maximum_sub_array approach')
array = [1, -3, 2, -5, 7, 6, -1, -4, 11, -23]
print(maximum_sub_array(array))

array = [-2, -3, -6, -12, -1, -52]
print(maximum_sub_array(array))

array = [2, 3, 6, 12, 1, 52]
print(maximum_sub_array(array))

# This is O(n) but also uses O(n) extra memory
# Dynamic solution based on: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=13s
def dynamic_maximum_sub_array(array):
	cache = [None for i in range(len(array))]
	cache[0] = array[0]
	for i in range(1, len(array)):
		cache[i] = max(array[i], array[i] + cache[i-1])
	return max(cache)

print('maximum_sub_array with dynamic programming approach')
array = [1, -3, 2, -5, 7, 6, -1, -4, 11, -23]
print(dynamic_maximum_sub_array(array))

array = [-2, -3, -6, -12, -1, -52]
print(dynamic_maximum_sub_array(array))

array = [2, 3, 6, 12, 1, 52]
print(dynamic_maximum_sub_array(array))

# O(n) only works if there at least one positive number
def kadane(array):
	sum = 0 
	max = float('-inf')
	start_idx = end_idx = None
	for element in array:
		if (sum + element) > 0:
			sum+=element
			if sum > max:
				max = sum
		else:
			sum = 0
			if element > max:
				max = element
	return max
print('kadane approach')
array = [1, -3, 2, -5, 7, 6, -1, -4, 11, -23]
print(kadane(array))
array = [-2, -3, -6, -12, -1, -52]
print(kadane(array))
array = [2, 3, 6, 12, 1, 52]
print(kadane(array))



