# Taken from: https://www.youtube.com/watch?v=-AMHUdZc9ss
# get all the set of 3 elements that sum 0

# This backtracking O(2^n)
def helper(array, selected_numbers, results):
	if len(selected_numbers) == 3 and sum(selected_numbers) == 0:
		results.append(selected_numbers)

	if len(selected_numbers) == 3 or len(array) == 0:
		return

	array_copy = array[:]
	current_element =  array_copy.pop()
	new_selected_numbers = selected_numbers[:]
	new_selected_numbers.append(current_element)

	helper(array_copy, selected_numbers, results)
	helper(array_copy, new_selected_numbers, results)

def three_sum(array):
	results = []
	initial_selection = []
	helper(array, initial_selection, results)
	return results

array = [-1, 0, 1, 2, -1, 4]
print('three sum of: ', array, ' is:')
print(three_sum(array))

# Video solution. O(n^2)

def merge(array, s, middle, e):
	lp = s

	while lp < middle+1:
		if array[middle+1] < array[lp]:
			array[lp], array[middle+1] = array[middle+1], array[lp]
			j = middle+1
			while j<e and array[j] > array[j+1]:
				j+=1
			array[j], array[middle+1] = array[middle+1], array[j]
		lp+=1
	return

def recursively_sort(array, s, e):
	if s>=e:
		return

	middle = int((s+e)/2)
	left = recursively_sort(array, s, middle)
	right = recursively_sort(array, middle+1, e)
	merge(array, s, middle, e)

def sort(array):
	recursively_sort(array, 0, len(array)-1)
# This O(n^2) no extra space required apart from the one to 
# store the solution
def three_sum_cuadratic(array):
	sort(array) # This is O(nlog(n))
	solutions = []
	for i in range(len(array)-2): # O(n^2)
		x = i + 1 # start pointer next element
		y = len(array)-1 # end pointer at the end

		while i == 0  and array[i] != array[i-1] and x != y:
			if (array[x] + array[y]) == -array[i]:
				solutions.append([array[i], array[x], array[y]])

			if (array[x] + array[y]) > -array[i]:
				last_y = array[y]
				while x != y and last_y == array[y]:
					y-=1
			else:
				last_x = array[x]
				while x != y and last_x == array[x]:
					x+=1
	return solutions

array = [-1, 0, 1, 2, -1, 4]
print('three_sum_cuadratic of: ', array, ' is:')
print(three_sum_cuadratic(array))



