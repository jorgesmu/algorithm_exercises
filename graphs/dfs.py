def prepare_data(graph):
	formatted_data = {}
	for edge in edges:
		if not edge['node1'] in formatted_data:
			formatted_data[edge['node1']] = []
		if not edge['node2'] in formatted_data:
			formatted_data[edge['node2']] = []
		formatted_data[edge['node1']].append(edge)
		formatted_data[edge['node2']].append(edge)
	return formatted_data

def dfs(edges_per_node, node):
	perform_dfs(edges_per_node, node, set())


def perform_dfs(edges_per_node, node, visited):
	if node not in visited:
		print(node)
		visited.add(node)
	for edge in edges_per_node[node]:
		if edge['node1'] not in visited:
			perform_dfs(edges_per_node, edge['node1'], visited)
		if edge['node2'] not in visited:
			perform_dfs(edges_per_node, edge['node2'], visited)

# Assuming nodes have a numeric id and a list of edged
# with weight, graph is being represented as an Adjacency list
# Graph taken from https://en.wikipedia.org/wiki/Depth-first_search
edges = [
	{
		'node1': 'A',
		'node2': 'B',
	},
	{
		'node1': 'B',
		'node2': 'D',
	},
	{
		'node1': 'B',
		'node2': 'F',
	},
	{
		'node1': 'A',
		'node2': 'C',
	},
	{
		'node1': 'C',
		'node2': 'G',
	},
	{
		'node1': 'A',
		'node2': 'E',
	},	
	{
		'node1': 'E',
		'node2': 'F',
	}
]

print('dfs for network: (expected result:  A, B, D, F, E, C, G. )')
print(dfs(prepare_data(edges), 'A'))
