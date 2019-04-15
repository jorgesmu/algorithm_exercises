# taken from: https://www.youtube.com/watch?v=Os5FM4KQtxw&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=14
from linked_list import Node

# time: O(n), space: O(2n)
def not_palim_recursive(li, queue):
	if not li:
		return False
	queue.append(li.value)
	not_palim = not_palim_recursive(li.next, queue)
	if li.value != queue.pop(0):
		return True
	if not_palim:
		return not_palim
	return False

def palindrome(li):
	queue = []
	return not not_palim_recursive(li, queue)


n4 = Node(5)
n3 = Node(4, n4)
n2 = Node(2, n3)
n1 = Node(4, n2)
palidrome_list = Node(5, n1)

print('palindrome for [5, 4, 2, 4, 5] is: ', palindrome(palidrome_list))

n5 = Node(5)
n6 = Node(4, n5)
n7 = Node(2, n6)
n8 = Node(1, n7)
not_palidrome_list = Node(5, n8)

print('palindrome for [5, 1, 2, 4, 5] is: ', palindrome(not_palidrome_list))

# Same implementation but iterative
def palindrome_stack_queue(li):
	stack = [] # this are represented and used as datastructures
	current_pointer = li
	while current_pointer:
		stack.append(current_pointer.value)
		current_pointer = current_pointer.next
	while li:
		if li.value != stack.pop():
			return False
		li = li.next
	return True

print('palindrome_stack_queue for [5, 4, 2, 4, 5] is: ', palindrome_stack_queue(palidrome_list))
print('palindrome_stack_queue for [5, 1, 2, 4, 5] is: ', palindrome_stack_queue(not_palidrome_list))

# x^y^x = y, iterating O(1.5*n), space: O(1)
def palindrome_xor_approach(li):
	xor_result = 0
	element_count = 0
	current_pointer = li
	runner = li

	while current_pointer:
		xor_result^=current_pointer.value
		element_count +=1
		current_pointer = current_pointer.next

	if element_count%2 ==0:
		return xor_result == 0

	# If odd number of elements we need to substract the middle
	# this is the same as using two pointers
	# this is the same approach as using two pointers as in the video
	pointer = 0
	while True:
		pointer+=1 
		if pointer == int(element_count/2)+1:
			return (li.value ^ xor_result) == 0
		li = li.next
print('palindrome_xor_approach for [5, 4, 2, 4, 5] is: ', palindrome_xor_approach(palidrome_list))
print('palindrome_xor_approach for [5, 1, 2, 4, 5] is: ', palindrome_xor_approach(not_palidrome_list))
