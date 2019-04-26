# taken from: https://www.youtube.com/watch?v=IPWmrjE1_MU&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=13&pbjreload=10

# Time and space: O(n!), we can redude space by
# doing the same iteratively instead of recursive

def rotate_right_sub_array(array, starting_point):
	last_element = array[len(array)-1]
	for j in range(len(array)-1, starting_point, -1):
		array[j] = array[j-1]
	array[starting_point]= last_element

def permutations_helper(array, pointer, results):
	if pointer == (len(array)-1):
		results.append(array[:])
	for i in range(pointer, len(array)):
		rotate_right_sub_array(array, pointer)
		permutations_helper(array, pointer+1, results)

def permutations(array):
	results = []
	permutations_helper(array, 0, results)
	return results

a = [1,2,3,4]
print('array: ', a, ' permutations:')
for permutation in permutations(a):
	print(permutation)