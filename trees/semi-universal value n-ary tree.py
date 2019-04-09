from tree import Tree
# taken from: https://www.youtube.com/watch?v=7HgsS8bRvjo
# n-ary tree

# O(n)
def get_value(tree, node_key):
	if node_key in tree:
		return tree[node_key]['value']
	return None


def universal_value_count(tree):
	_, count = count_unival_in_tree(tree, set())
	return count


def count_unival_in_tree(tree, found_values):
	current_subset = found_values.copy()
	if len(tree.children) == 0:
		current_subset.add(tree.value)
		return current_subset, 1

	sum = 0
	is_semival = True
	for children in tree.children:
		sub_tree_subset, subtree_count = count_unival_in_tree(children, current_subset)
		sum+=subtree_count
		current_subset = current_subset.union(sub_tree_subset)
	current_subset.add(tree.value)
	if len(current_subset) <= 2:
		sum+=1
	return current_subset, sum


root = Tree(3)
t2 = Tree(1)
t3 = Tree(3)
t10 = Tree(43)
t4 = Tree(1)
t5 = Tree(1)
t6 = Tree(3)
t7 = Tree(1)
t8 = Tree(1)
t9 = Tree(1)

t4.children.extend([t7, t8, t9])
t3.children.extend([t4, t5, t6])
root.children.extend([t2, t3, t10])
print(universal_value_count(root))