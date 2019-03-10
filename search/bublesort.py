# Time complexity O(n^2), memory usage(n + c). c=swap buffer size
def bublesort(collection):
	for i in range(0, len(collection)):
		for j in range(i+1, len(collection)):
			if collection[i] > collection[j]:
				swap_buffer = collection[j]
				collection[j] = collection[i]
				collection[i] = swap_buffer

	return collection

collection = [1, 3, 23, 42, -2, 1234, 6, 7, 6]
print(bublesort(collection))


