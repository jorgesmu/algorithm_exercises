# Taken from: https://www.youtube.com/watch?v=hLcYp67wCcM&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=17

# Time O(n), time: O(n)
def zero_sub_array(array):
	seen = {}
	sum = 0
	for i in range(len(array)):
		sum += array[i]
		if sum in seen:
			return array[seen[sum]+1:i+1]
		else:
			seen[sum] = i
	return None


array = [1, 2, -5, 1, 2, -1]
print('Array: ', array)
print('zero_sub_array: ', zero_sub_array(array))