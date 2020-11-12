# Taken from: https://www.youtube.com/watch?v=P_YMAJWEK3Q
# making solution for n-ary trees

from tree import Tree

# Complexity O(n)
def print_by_level(root):
	level = 0
	queue = [(root, level)]
	while len(queue) > 0:
		node, level = queue.pop(0)
		print("{}: {}".format(str(level+1), str(node.value)))
		for child in node.children:
			queue.append((child, level+1))


root = Tree(2)
t2 = Tree(3)
t3 = Tree(4)
t5 = Tree(1)
t6 = Tree(2)
t7 = Tree(5)

root.children.extend([t2, t3])
t2.children.extend([t5])
t3.children.extend([t6, t7])
print_by_level(root)