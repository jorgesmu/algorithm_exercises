class Node:
	def __init__(self, value=None, next=None, random=None):
		self.value = value
		self.next = next
		self.random = random

# From the video
# O(n)
def clone(li):
	if not li:
		return None

	# first iteration: duplicate nodesa
	current_node = li
	while current_node:
		new_node = Node(current_node.value)
		temp = current_node.next
		current_node.next = new_node
		new_node.next = temp

		current_node = current_node.next.next
	# second iteration: set random pointers
	current_node = li
	while current_node:
		current_node.next.random = current_node.random.next
		current_node = current_node.next.next

	# Third iteration: split lists
	current_node = li
	copy = li.next
	while current_node and current_node.next:
		temp = current_node.next
		current_node.next = current_node.next.next 
		if current_node.next:
			temp.next = current_node.next.next
		else:
			temp.next = None
		current_node = current_node.next
	return copy

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n1.random = n3
n2.next = n3
n2.random = n1
n3.next = n4
n3.random = n3
n4.random = n2

new_node = clone(n1)
while new_node:
	print('value: ', new_node.value)
	if new_node.next:
		print('next: ', new_node.next.value)
	if new_node.random:
		print('random: ', new_node.random.value)
	new_node = new_node.next
