# Taken from:  https://www.youtube.com/watch?v=zplklOy7ENo
# O(n*k) being k the number of lists

# finding min and max is O(l)
def find_range(lists, pointers):
	min = float('inf')
	min_list = None
	max = float('-inf')
	for i in range(len(pointers)):
		element = lists[i][pointers[i]]
		if element < min:
			min = element
			min_list = i
		if element > max:
			max = element
	return min, max, min_list

def increment_min(lists, min_list, pointers):
	pointers[min_list] += 1
	if pointers[min_list] >= len(lists[min_list]):
		return None, None, None
	return find_range(lists, pointers)

def shortest_range(lists):
	pointers = []
	for list in lists:
		if len(list) == 0:
			return None
		pointers.append(0)
	min, max, min_list = find_range(lists, pointers)
	min_range = min
	while(min_range != None):
		min_range, max_range, min_list = increment_min(lists, min_list, pointers)
		if min_range and (max_range - min_range) < (max-min):
			min, max = min_range, max_range
	return min, max
l1 = [4, 10, 15, 24]
l2 = [0, 9, 12, 20]
l3 = [5, 18, 22, 30]

lists = [l1, l2, l3]

print(shortest_range(lists))