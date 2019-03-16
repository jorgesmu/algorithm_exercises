from heap import Heap

def should_add_edge(visited_edges, edge):
	# This checks that no cycle is being generated
	return edge['node1'] not in visited_edges or edge['node2'] not in visited_edges


def edges_heap(edges):
	inequality = lambda x,y: x["cost"] < y["cost"]
	return Heap(edges, inequality) # Heap mins


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

# Complexity O(E log V). This implementation just provides the minimum
# spanning tree. If the graph would have more than one component it will return null
# If want to change this we need to have one set per node and merge sets ones we connect
# components
def prim(nodes, edges_per_node, starting_node):
	heap = edges_heap(edges_per_node[starting_node])
	visited = set([starting_node])
	cost = 0
	edges = []
	while len(visited) < nodes and heap.size() > 0:
		edge = heap.pop()
		if should_add_edge(visited, edge):
			cost += edge['cost']
			edges.append(edge)
			if edge['node1'] not in visited:
				heap.push_all(edges_per_node[edge['node1']])
			if edge['node2'] not in visited:
				heap.push_all(edges_per_node[edge['node2']])
			visited.add(edge['node1'])
			visited.add(edge['node2'])
	if len(visited) < nodes:
		cost = None
		edges = None
	return {'cost': cost, 'edges': edges}		


# Assuming nodes have a numeric id and a list of edged
# with weight, graph is being represented as an Adjacency list
nodes = 4
edges = [
	{
		'node1': 1,
		'node2': 2,
		'cost': 3
	},
	{
		'node1': 1,
		'node2': 3,
		'cost': 10
	},
	{
		'node1': 1,
		'node2': 4,
		'cost': 8
	},
	{
		'node1': 2,
		'node2': 3,
		'cost': 6
	},
	{
		'node1': 2,
		'node2': 4,
		'cost': 2
	},
	{
		'node1': 3,
		'node2': 4,
		'cost': 543
	}
]

print('Prim for network:')
print(prim(nodes, prepare_data(edges), 1))
