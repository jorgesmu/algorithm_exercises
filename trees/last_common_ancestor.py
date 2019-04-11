# taken from: https://www.youtube.com/watch?v=GnliEfQo114&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=10&t=0s
from tree import Tree

def path_to(node, n):
	if node.value == n:
		return [n]
	for child in node.children:
		child_path = path_to(child, n)
		if child_path:
			partial_path = [node.value]
			partial_path.extend(child_path)
			return partial_path
	return None

def find_lca_from_paths(path_to_n1, path_to_n2):
	lca = None
	while len(path_to_n1) > 0 and len(path_to_n2) > 0 and path_to_n1[0] == path_to_n2[0]:
		lca = path_to_n1[0]
		path_to_n1.pop(0)
		path_to_n2.pop(0)
	return lca

# O(n)
def lca(tree, n1, n2):
	if n1 == n2:
		return n1
	path_to_n1 = path_to(tree, n1)
	path_to_n2 = path_to(tree, n2)
	return find_lca_from_paths(path_to_n1, path_to_n2)


root = Tree(1)
t2 = Tree(2)
t3 = Tree(3)
t4 = Tree(4)
t5 = Tree(5)
t6 = Tree(6)

root.children.extend([t2, t3])
t3.children.extend([t4, t6])
t6.children.extend([t5, t6])

print('lca for tree for nodes 4, 5 is:', lca(root, 4, 5))
print('lca for tree for nodes 3, 5 is:', lca(root, 3, 5))
print('lca for tree for nodes 4, 2 is:', lca(root, 4, 2))
print('lca for tree for nodes 6, 6 is:', lca(root, 6, 6))