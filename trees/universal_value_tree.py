# taken from: https://www.youtube.com/watch?v=7HgsS8bRvjo
# asumming its a binary tree only. 

# O(n)
def get_value(tree, node_key):
	if node_key in tree:
		return tree[node_key]['value']
	return None


def universal_value_count(tree):
	_, count = count_unival_in_tree(tree, 'root')
	return count


def count_unival_in_tree(tree, node_key):
	if not node_key:
		return True, 0

	node = tree[node_key]
	if not node['right'] and not node['left']:
		return True, 1

	is_left, left_count = count_unival_in_tree(tree, node['left'])
	is_right, right_count = count_unival_in_tree(tree, node['right'])
	
	sum = left_count + right_count
	is_universal = False
	
	left_value = get_value(tree, node['left'])
	right_value = get_value(tree, node['right'])
	current_value = get_value(tree, node_key)
	if is_left and is_right and left_value == right_value and right_value == current_value:
		sum+=1
		is_universal = True
	return is_universal, sum


tree = {
	'root': {
		'left': 1,
		'right': 2,
		'value': 4
	},
	1: {
		'left': None,
		'right': None,
		'value': 1 
	},
	2: {
		'left': 3,
		'right': 4,
		'value': 34 
	},
	3: {
		'left': 5,
		'right': 6,
		'value': 1 
	},
	4: {
		'left': None,
		'right': None,
		'value': 65
	},
	5: {
		'left': None,
		'right': None,
		'value': 1 
	},
	6: {
		'left': None,
		'right': None,
		'value': 1
	},
}
print(universal_value_count(tree))