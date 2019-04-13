# Taken from: https://www.youtube.com/watch?v=dQsZP8UvHVk
from stack import Stack

# O(n) in both time and space. Asumming we can use other stack (same datastructure)
def recursive_reverse(stack, result_stack):
	if stack.size() == 0:
		return
	element = stack.pop()
	result_stack.push(element)
	recursive_reverse(stack, result_stack)
	stack.push(element)
	return

def reverse(stack):
	result_stack = Stack()
	recursive_reverse(stack, result_stack)
	return result_stack

# from the video: using no other stack
def reverse_in_place(stack):
	if stack.size() == 0:
		return
	element = stack.pop()
	reverse_in_place(stack)
	push_element_to_the_bottom(stack, element)
	return

def push_element_to_the_bottom(stack, element):
	if stack.size() == 0:
		stack.push(element)
		return
	popped_element = stack.pop()
	push_element_to_the_bottom(stack, element)
	stack.push(popped_element)
	return

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('stack before reversing: ', stack.array)
result_stack = reverse(stack)
print('after reversing: ', result_stack.array)

print('stack before reversing: ', stack.array)
reverse_in_place(stack)
print('after reversing in place: ', stack.array)