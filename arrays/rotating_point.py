# https://www.youtube.com/watch?v=4qjprDkJrjY

def helper(array, start, end):
	import pdb; pdb.set_trace()
	if array[start] <= array[end]:
		return start
	n = len(array)
	middle = int((start+end)/2)
	previous_pos = (middle + n-1)%n
	next_pos  = (middle + +1)%n
	if array[previous_pos] > array[middle] and array[next_pos] > array[middle]:
		return middle

	if array[middle] < array[start]:
		return helper(array, start, middle-1)
	return helper(array, middle+1, end)

# O(log n)
def find_rotating_point(array):
	return helper(array, 0, len(array)-1)

a = [3, 5, 8 , 11, 12, 2]
print('array: ', a)
rotating_point = find_rotating_point(a)
print('find_rotating_point: ', rotating_point)
print('first element: ', a[rotating_point])