# Taken from: https://www.youtube.com/watch?v=r2Vn6ztdSP0

from tree import Tree

def helper(tree, depth, last_value):
	if last_value != tree.value-1:
		depth = 1

	maximum_depth = depth
	for child in tree.children:
		child_max_depth = helper(child, depth + 1, tree.value)
		if child_max_depth > maximum_depth:
			maximum_depth = child_max_depth
	return maximum_depth

def lcb(root):
	return helper(root, 0, None)

root = Tree(0)
t1 = Tree(1)
t2 = Tree(2)
t3 = Tree(1)
t4 = Tree(2)
t5 = Tree(1)
t6 = Tree(3)

t7 = Tree(4)
t6.children = [t7]
t8 = Tree(5)
t7.children = [t8]
root.children.extend([t1, t2])
t1.children.extend([t3, t4])
t2.children.extend([t5, t6])

print('longest consecutive branch is: ', lcb(root))