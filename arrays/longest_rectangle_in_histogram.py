# taken from: https://www.youtube.com/watch?v=RVIh0snn4Qc&t=481s
from stack import Stack

def find_max(histogram, stack, max, index, lower_limit):
	while stack.size() > 0 and histogram[stack.seek()] > lower_limit:
		stack_index = stack.pop()
		local_max = (index-stack_index)*histogram[stack_index]
		if local_max > max:
			max = local_max
	return max

def longest_rectangle(histogram):
	if len(histogram) == 0:
		return 0
	max = -1 # Histogram can cointain natural values only
	incresing_stack = Stack()
	for i in range(len(histogram)):
		if i == 0 or histogram[i] > histogram[i-1]:
			incresing_stack.push(i)
		elif histogram[i] < histogram[i-1]:
			max = find_max(histogram, incresing_stack, max, i, histogram[i])
	return find_max(histogram, incresing_stack, max, i+1, 0)


h1 = [1, 2, 3, 4, 5, 3, 3, 2]
print('Longest rectlangle for histogram ', h1, ' is:')
print(longest_rectangle(h1))


h2 = [1, 2, 3, 4, 5, 3, 3, 2, 0, 5, 5, 5, 5, 0, 2 ,3, 5]
print('Longest rectlangle for histogram ', h2, ' is:')
print(longest_rectangle(h2))

h3 = [5, 2, 1]
print('Longest rectlangle for histogram ', h3, ' is:')
print(longest_rectangle(h3))