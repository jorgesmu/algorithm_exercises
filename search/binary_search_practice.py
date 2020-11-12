# O(logn), no extra space required

def binary_search(sorted_array, key, low, high):
	if high < low:
		return False
	middle = (low + high) // 2
	if sorted_array[middle] == key:
		return True
	elif sorted_array[middle] > key:
		return binary_search(sorted_array, key, low, middle-1)
	return binary_search(sorted_array, key, middle+1, high)
array = [1, 3, 5, 7, 9, 11]
print(array)
print(binary_search(array, 1234, 0, len(array)-1))
print(binary_search(array, 11, 0, len(array)-1))
print(binary_search(array, 6, 0, len(array)-1))
print(binary_search(array, 7, 0, len(array)-1))