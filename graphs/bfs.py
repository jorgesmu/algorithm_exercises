def prepare_data(graph):
	formatted_data = {}
	for edge in edges:
		if not edge['node1'] in formatted_data:
			formatted_data[edge['node1']] = []
		if not edge['node2'] in formatted_data:
			formatted_data[edge['node2']] = []
		formatted_data[edge['node1']].append(edge['node2'])
		formatted_data[edge['node2']].append(edge['node1'])
	return formatted_data

def bfs(neighbors, queue, visited):
	if len(queue) == 0:
		return
	element = queue.pop(0)
	if element not in visited:
		print(element)
		visited.add(element)
		queue = queue + neighbors[element][:]
	bfs(neighbors, queue, visited)

	
# O(V + E)
# Assuming nodes have a numeric id and a list of edged
# with weight, graph is being represented as an Adjacency list
# Graph taken from https://en.wikipedia.org/wiki/Breadth-first_search
edges = [
	{
		'node1': 'A',
		'node2': 'B',
	},
	{
		'node1': 'A',
		'node2': 'C',
	},
	{
		'node1': 'B',
		'node2': 'D',
	},
	{
		'node1': 'B',
		'node2': 'E',
	},
	{
		'node1': 'C',
		'node2': 'F',
	},
	{
		'node1': 'C',
		'node2': 'G',
	},
	{
		'node1': 'E',
		'node2': 'H',
	}
]

print('bfs for network: (expected result:  A, B, c, D, E, F, G, H )')
bfs(prepare_data(edges), ['A'], set())
