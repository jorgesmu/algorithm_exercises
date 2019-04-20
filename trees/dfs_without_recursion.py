# Taken from: https://www.youtube.com/watch?v=MZ67ceIH8v4&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=50
from tree import BinaryTree

def append_with_left_childs(stack, node):
	stack.append(node)
	current_node = node
	while current_node.left_child:
		stack.append(current_node.left_child)
		current_node = current_node.left_child

# O(n) in time and O(n) in space
def inorder_transversal(tree):
	stack = [] # using array as a stack
	append_with_left_childs(stack, tree)
	while len(stack) > 0:
		element = stack.pop()
		print(element.value)
		if element.right_child:
			append_with_left_childs(stack, element.right_child)

n8 = BinaryTree(8)
n6 = BinaryTree(6)
n4 = BinaryTree(4)
n1 = BinaryTree(1)
n7 = BinaryTree(7, n6, n8)
n3 = BinaryTree(3, n1, n4)
root = BinaryTree(5, n3, n7)
print('inorder_transversal should print 1, 3, 4, 5, 6, 7, 8')
inorder_transversal(root)