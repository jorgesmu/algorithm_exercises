# Taken from: https://www.youtube.com/watch?v=P_YMAJWEK3Q
# making solution for n-ary trees

from tree import Tree

# Complexity O(n)
def print_by_level(root):
	level = 0
	buffer = ''
	queue = [(root, level)]

	while len(queue) > 0:
		node, node_level = queue.pop(0)
		if node_level != level:
			print(buffer)
			buffer = ''
			level = node_level
		buffer += str(node.value) + ' '
		for child in node.children:
			queue.append((child, node_level + 1))
	print(buffer)
	return

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