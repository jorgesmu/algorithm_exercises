# taken from: https://www.youtube.com/watch?v=nqlNzOcnCfs&t=130s
# Assuming the question is to count the number of subsets
# up to n given a an array of size m.
# This solution is O(n*m) and takes O(2n) extra memory

def count_subsets_up_to_n(array, n):
	cache = [0 for i in range(n+1)]
	for idx in range(len(array)):
		cache[array[idx]]+=1
		cache_copy = cache[:]
		for i in range(n+1):
			if array[idx] != i and i+array[idx] <= n and cache_copy[i]>0:
				cache[i+array[idx]]+=cache_copy[i]
	return cache[n]

array = [2, 4, 6, 10]
n = 16

print('array: ', array, " n: ", n)
print(count_subsets_up_to_n(array, n))