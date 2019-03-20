import time

def build_adjacencies(nodes, graph):
	result = {}
	for i in range(1,nodes+1):
		result[i] = []
	for edge in graph:
		v1 = edge['node1']
		v2 = edge['node2']
		result[v1].append(v2)
		result[v2].append(v1) 
	return result


def is_valid(node, current_coloring, neighbors):
	node_color = current_coloring[node]
	for neighbor in neighbors[node]:
		if neighbor in current_coloring and current_coloring[neighbor] == node_color:
			return False
	return True


def backtracking_coloring(results, node, nodes, coloring, neighbors, colors):
	current_coloring = coloring.copy()	
	for color in range(colors):
		current_coloring[node] = color
		if is_valid(node, current_coloring, neighbors):
			if len(current_coloring) == nodes:
				results.append(current_coloring)
			else:
				[backtracking_coloring(results, neighbor, nodes, current_coloring, neighbors, colors) for neighbor in neighbors[node] if neighbor not in current_coloring]

# This implementation assumes that the graph has only one component
# This solution is O(n) but might lead to a non optimal coloring depending on
# the order in which we process the nodes
def coloring(nodes, graph, colors):
	results = []
	if nodes == 0 or colors == 0:
		return
	coloring = {}
	neighbors = build_adjacencies(nodes, graph)
	empty_coloring = {}
	backtracking_coloring(results, 1, nodes, empty_coloring, neighbors, colors)
	return results
# Nodes are 1 indexed
graph = [
	{
		'node1': 1,
		'node2': 2
	},
	{
		'node1': 1,
		'node2': 3
	},
	{
		'node1': 1,
		'node2': 4
	},
	{
		'node1': 2,
		'node2': 3
	},
	{
		'node1': 3,
		'node2': 4
	},
	{
		'node1': 5,
		'node2': 4
	},
	{
		'node1': 5,
		'node2': 2
	},
	{
		'node1': 5,
		'node2': 1
	},
	{
		'node1': 6,
		'node2': 4
	}
]

def execute(colors):
	print('coloring for graph ({0} color available)'.format(colors))
	start = time.time()
	solutions = coloring(6, graph, colors)
	end = time.time()
	time_used = round((end - start), 2)
	print('found solutions: {0}, in {1}s'.format(len(solutions), time_used))

execute(1)
execute(2)
execute(3)
execute(4)
execute(5)
execute(6)
execute(7)
execute(8)
execute(9)
execute(10)
execute(15)
execute(16)
execute(17)
