# Complexity: O(n^2)
def partition(collection, low, high):
	pivot = collection[high]
	i = low
	for j in range(low,high):
		if collection[j] < pivot:
			collection[j], collection[i] = collection[i], collection[j]
			i+=1
	collection[i], collection[high] = collection[high], collection[i]
	return i

def quicksort(collection, low, high):
	if low > high:
		return
	pivot_index = partition(collection, low, high)
	quicksort(collection, low, pivot_index-1)
	quicksort(collection, pivot_index+1, high)
	return collection
collection = [1, 3, 23, 42, -2, 1234, 6, 7, 6]
print(quicksort(collection, 0, len(collection)-1))