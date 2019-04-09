# taken from: https://www.youtube.com/watch?v=nqlNzOcnCfs&t=130s
# Assuming the question is to find all the subset that sum n given an
# array of lenght m
# we are using backtracking, for each element in the array I need to make a desicion,
# even we include it or not in the final set
# This solution is O(2^m) 

def find_sets(array, n):
	found_sets = []
	find_sets_recursively(array, n, found_sets, [])
	return found_sets

def find_sets_recursively(array, n, found_sets, current_set):
	if sum(current_set) == n:
		found_sets.append(current_set)
	if sum(current_set) >= n or len(array) == 0:
		return
	new_array = array[:]
	element = new_array.pop(0)
	find_sets_recursively(new_array, n, found_sets, current_set)
	add_elment_set = current_set.copy()
	add_elment_set.append(element)
	find_sets_recursively(new_array, n, found_sets, add_elment_set)

array = [1, 5, 3, 2, 4, 10, 6]
n = 16

print('array: ', array, " n: ", n)
print(find_sets(array, n))