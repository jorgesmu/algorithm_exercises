# taken from: https://www.youtube.com/watch?v=nqlNzOcnCfs&t=130s
# Assuming the question is to find all the subset that sum n given an
# array of lenght m
# we are using backtracking, for each element in the array I need to make a desicion,
# even we include it or not in the final set
# This solution is O(2^m) 

def find_subsets_rec(buffer, i, array, n):
	k = "{}:{}".format(i, n)
	if k in buffer:
		return buffer[k]
	if i < 0 or n < 0:
		res =  0
	elif n == array[i]:
		res = 1 + find_subsets_rec(buffer, i-1, array, n)
	else:
		res = find_subsets_rec(buffer, i-1, array, n) + find_subsets_rec(buffer, i-1, array, n - array[i])
	buffer[k] = res
	return buffer[k]

def find_sets(array, n):
	buffer = {}
	return find_subsets_rec(buffer, len(array)-1, array, n)

array = [1, 2, 3, 4, 5, 6, 10, 16]
n = 16

print('array: ', array, " n: ", n)
print(find_sets(array, n))