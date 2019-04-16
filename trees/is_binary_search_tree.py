from random_binary_tree import BinaryTree
def is_binary_helper(tree, min, max):
	if not tree:
		return True
	if tree.value() < min or tree.value() > max:
		return False
	return is_binary_helper(tree.left_child(), min, tree.value()) and is_binary_helper(tree.right_child(), tree.value() + 1, max)

def is_binary_search_tree(tree):
	return is_binary_helper(tree, float('-inf'), float('inf'))

root = BinaryTree(7)
t2 = BinaryTree(3)
t3 = BinaryTree(9)
t4 = BinaryTree(2)
t5 = BinaryTree(5)
t6 = BinaryTree(4)
t7 = BinaryTree(20)

#	  7
#  3      9
# 2 5    4 20

t3.set_left_child(t6)
t3.set_right_child(t7)
t2.set_left_child(t4)
t2.set_right_child(t5)
root.set_left_child(t2)
root.set_right_child(t3)

print('is binary search tree for a non binary search tree: ', is_binary_search_tree(root))
t6_2 = BinaryTree(8)
t3.set_left_child(t6_2)

#	  7
#  3      9
# 2 5    8 20
print('is binary search tree for a binary search tree: ', is_binary_search_tree(root))