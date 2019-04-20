# Taken from: https://www.youtube.com/watch?v=IR2X5Mw3StY&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=23
from linked_list import Node

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

def print_reversed_recursive(list):
	if not list:
		return None
	print_reversed_recursive(list.next)
	print(list.value)
	return

print('print reversed recursive for 1 -> 2 -> 3 -> 4 -> 5 is: ')
print_reversed_recursive(n1)

def reverse(list):
	previous = None
	while list:
		next = list.next
		list.next = previous
		previous = list
		list = next
	return previous

def print_reversed_reversing(list):
	list = reverse(list)
	node = list
	while node:
		print(node.value)
		node = node.next
	reverse(list) # return it to the origianl state
	return

print('print reversed (reversing) for 1 -> 2 -> 3 -> 4 -> 5 is: ')
print_reversed_reversing(n1)