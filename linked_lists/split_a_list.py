# Taken from: https://www.youtube.com/watch?v=lMxYBLqt1Mg&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=10
from linked_list import Node

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

# This runs on O(n) time and O(1) space
def split(list):
	if not list:
		return None
	slow = list
	fast = list.next
	# Will keep longer half on the left side on odd number of elements
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	second_half = slow.next
	slow.next = None
	return second_half

print('list 1 -> 2 -> 3 -> 4')
print('first node for second half: ', split(n1).value)

n5 = Node(5)
n4.next = n5
print('list 1 -> 2 -> 3 -> 4 -> 5')
print('first node for second half: ', split(n1).value)