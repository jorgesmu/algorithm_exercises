# O(logn), no extra space required

def binary_search(sorted_array, key, low, high):
	middle = int((low + high)/2)
	looked_element = sorted_array[middle]
	if len(sorted_array) == 0 or low > high:
		return None
	if key == looked_element: # elements in the array are ints but could be a key to a complex object
		return looked_element
	if key < looked_element:
		return binary_search(sorted_array, key, low, middle-1)
	else:
		return binary_search(sorted_array, key, middle+1, high)

array = [1, 3, 5, 7, 9, 11]
print(array)
print(binary_search(array, 1234, 0, len(array)-1))
print(binary_search(array, 11, 0, len(array)-1))
print(binary_search(array, 6, 0, len(array)-1))
print(binary_search(array, 7, 0, len(array)-1))