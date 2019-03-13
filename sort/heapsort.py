# Complexity heapsort O(nlogn)

def perform_heapsort(array, max):
	heapify(array)

	for current_max in range(max, 0, -1):
		array[0], array[current_max] = array[current_max], array[0]
		sift_down(array, current_max-1)


# sift_down is log(n)
def sift_down(array, max, current_index = 0):
	if max == 0:
		return
	left_index = left_child(current_index) 
	while(left_index <= max):
		swap_index = current_index
		if array[left_index] > array[swap_index]:
			swap_index = left_index
		right_index = right_child(current_index)
		if right_index <= max and array[right_index] > array[swap_index]:
			swap_index = right_index
		if swap_index == current_index:
			return
		array[swap_index], array[current_index] = array[current_index], array[swap_index]
		current_index = swap_index
		left_index = left_child(current_index)
	return


def parent(index):
	return int((index-1)/2)


# Heapify is O(n)
def heapify(array):
	max_index = len(array) - 1
	first_parent = parent(max_index - 1)
	for i in range(first_parent, -1, -1):
		sift_down(array, max_index, i)


def left_child(index):
	return 2*index + 1


def right_child(index):
	return 2*index + 2


def heapsort(array):
	perform_heapsort(array, len(array)-1)
	return array


array = [5, 9, 15, 3, 2, 1, 10]
print(array)
print(heapsort(array))


array = [5, 9, 10, 3, 2, 1, 15]
print(array)
print(heapsort(array))
