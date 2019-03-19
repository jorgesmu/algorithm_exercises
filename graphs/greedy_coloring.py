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

def select_color(colors, neighbors_coloring_set):
	for color in range(colors):
		if color not in neighbors_coloring_set:
			return color
	return None

# This solution is O(n) but might lead to a non optimal coloring depending on
# the order in which we process the nodes
def coloring(nodes, graph, colors):
	coloring = {}
	neighbors = build_adjacencies(nodes, graph)
	for node in range(1,nodes+1):
		neighbors_coloring_set = set()
		[neighbors_coloring_set.add(coloring[neighbor]) for neighbor in neighbors[node] if neighbor in coloring]
		selected_color = select_color(colors, neighbors_coloring_set)
		if selected_color is None:
			return selected_color
		coloring [node] = selected_color
	return coloring

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
		'node1': 2,
		'node2': 4
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

print("coloring for graph (1 color available)")
print(coloring(6, graph, 1))
print("coloring for graph (2 colors available)")
print(coloring(6, graph, 2))
print("coloring for graph (3 colors available)")
print(coloring(6, graph, 3))
print("coloring for graph (4 colors available)")
print(coloring(6, graph, 4))
print("coloring for graph (5 colors available)")
print(coloring(6, graph, 5))
print("coloring for graph (6 colors available)")
print(coloring(6, graph, 6))
