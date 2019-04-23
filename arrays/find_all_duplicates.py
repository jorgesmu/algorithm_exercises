# Taken from: https://www.youtube.com/watch?v=GeHOlt_QYz8&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=48

# Time: O(n), O(1)
def find_all_duplicates(array):
	result = set()
	for i in range(len(array)):
		element = array[i]
		if not element in result:
			if array[element-1] > 0:
				array[element-1]*=-1
			else:
				result.add(element)

	for i in range(len(array)):
		array[i] = abs(array[i])
	return list(result)

array = [5, 1, 2, 2, 3, 1, 4, 3, 2, 1]

print('Array: ', array)
print('duplicates: ', find_all_duplicates(array))
print('Array after: ', array)