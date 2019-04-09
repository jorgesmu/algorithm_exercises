from tree import Tree
# taken from: https://www.youtube.com/watch?v=7HgsS8bRvjo
# n-ary tree

# O(n)
def get_value(tree, node_key):
	if node_key in tree:
		return tree[node_key]['value']
	return None


def universal_value_count(tree):
	_, count = count_unival_in_tree(tree)
	return count


def count_unival_in_tree(tree):
	if len(tree.children) == 0:
		return True, 1

	sum = 0
	is_unival = True
	for children in tree.children:
		is_sub_tree_unival, subtree_count = count_unival_in_tree(children)
		sum+=subtree_count
		if not is_sub_tree_unival or children.value != tree.value:
			is_unival = False
	if is_unival:
		sum+=1
	return is_unival, sum


root = Tree(3)
t2 = Tree(1)
t3 = Tree(3)
t4 = Tree(1)
t5 = Tree(1)
t6 = Tree(4)
t7 = Tree(1)
t8 = Tree(1)
t9 = Tree(1)

t4.children.extend([t7, t8, t9])
t3.children.extend([t4, t5, t6])
root.children.extend([t2, t3])
print(universal_value_count(root))