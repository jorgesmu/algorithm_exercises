def calculate_subsets(subsets, current_set):
	if len(current_set) == 0:
		subsets.append(current_set)
		return
	element = current_set.pop()
	calculate_subsets(subsets, current_set)
	for subset in subsets.copy():
		new_subset = subset.copy()
		new_subset.add(element)
		subsets.append(new_subset)
	return 

def find_subsets(current_set):
	subsets = []
	calculate_subsets(subsets, current_set)
	return subsets


current_set = {1, 2, 3, 4}
print('set:')
print(current_set)
print('number of subsets:')
subsets = find_subsets(current_set)
print(len(subsets))
print(subsets)