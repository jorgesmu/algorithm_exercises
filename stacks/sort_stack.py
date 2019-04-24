# Taken from: https://www.youtube.com/watch?v=nll-b4GeiX4&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=24

from stack import Stack

def push_in_order(stack, element):
	if not element:
		return
	if stack.size() == 0 or stack.seek() > element:
		stack.push(element)
		return
	current_element = stack.pop()
	push_in_order(stack, element)
	stack.push(current_element)
	return

# Time: O(n^2), space: O(1) + recursive stack calls
def sort(stack):
	aux_stack = Stack()
	while stack.size() > 0:
		push_in_order(aux_stack, stack.pop())
	return aux_stack


s = Stack()
s.push(5)
s.push(9)
s.push(1)
s.push(2)
s.push(3)
s.push(6)
s.push(7)
s.push(8)
s.push(10)
s.push(4)
# print('stack is 5, 9, 1, 2, 3, 6, 7, 8, 10, 4')
# print('poping after sort is:')
# sorted_stack = sort(s)

# while sorted_stack.size() > 0:
# 	print(sorted_stack.pop())

# From the video:

def sort_iteratively(stack):
	aux_stack = Stack()
	while stack.size() > 0:
		element = stack.pop()
		while aux_stack.size() > 0 and aux_stack.seek() < element:
			stack.push(aux_stack.pop())
		aux_stack.push(element)
	return aux_stack


print('stack is 5, 9, 1, 2, 3, 6, 7, 8, 10, 4')
print('poping after iterative sort is:')
sorted_stack = sort(s)
while sorted_stack.size() > 0:
	print(sorted_stack.pop())
