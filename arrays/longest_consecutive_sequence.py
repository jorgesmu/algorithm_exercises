# Taken from: https://www.youtube.com/watch?v=VeJOswJTDos

# O(n) as we are iterating over the structure twice
# We are using o(n) extra space as well for constructing
# the set

def longest_con_seq(array):
	max_seq = 0
	num_set = set(array)
	for num in num_set:
		if not (num-1) in num_set:
			count = 0
			while (num+count) in num_set:
				count+=1
			max_seq = max(max_seq, count)
	return max_seq

array = [60, 2, 1, 5, 9, 10, 4, 3, 65, 62, 63]
print('longest consecutive sequence for: ', array, ' is: ', longest_con_seq(array))