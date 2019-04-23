# Taken from: https://www.youtube.com/watch?v=Dte6EF1nHNo&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=27

class Node:
	def __init__(self, value):
		self.left_node = self.right_node = None
		self.value = value

def concatenate(a, b):
	if a == None:
		return b
	if b == None:
		return a

	a_end = a.left_node
	b_end = b.left_node

	a.left_node = b_end
	b_end.right_node = a

	b.left_node = a_end
	a_end.right_node = b
	return a

def tree_to_list(tree):
	if not tree:
		return tree

	left_list = tree_to_list(tree.left_node)
	right_list = tree_to_list(tree.right_node)
	tree.left_node = tree
	tree.right_node = tree
	left_new_circular_list = concatenate(left_list, tree)
	return concatenate(left_new_circular_list, right_list)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left_node = n2
n1.right_node = n3
n2.left_node = n4
n2.right_node = n5
n3.left_node = n6
n3.right_node = n7

n = tree_to_list(n1)

print('Expected list should be 4,2,5,1,6,3,7,4,..')
for i in range(20):
	print(n.value)
	n = n.right_node