def is_bipartite(graph, starting_node):
	colored = {}
	next_colors = {0:1, 1:0} # 2 problem coloring
	queue = [(starting_node, 0)] # (node to process, color to assign)
	while(len(queue) > 0):
		node, color = queue.pop(0)
		if node not in colored:
			colored[node] = color
			next_color = next_colors[color]
			for neighbor in graph[node]:
				if neighbor in colored and colored[neighbor] != next_color:
					return False
				queue.append((neighbor, next_color))
	return True


bipartite_graph = {
	1: [4, 5],
	2: [4],
	3: [4, 5],
	4: [1, 2 ,3],
	5: [1, 3]
}

print("Is bipartite for a bipartite graph:")
print(is_bipartite(bipartite_graph, 1))

non_bipartite_graph = {
	1: [4, 5],
	2: [4],
	3: [4, 5],
	4: [1, 2 ,3, 5],
	5: [1, 3, 4]
}

print("Is bipartite for a non bipartite graph:")
print(is_bipartite(non_bipartite_graph, 1))