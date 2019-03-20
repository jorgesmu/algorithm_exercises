from heap import Heap

def find_my_way_back(graph, starting_city, current_city):
	paths = graph[current_city]
	for path in paths:
		if path[0] == starting_city:
			return path
	return None

def calculate_next_city(graph, path, current_city):
	inequality = lambda x,y: x[1] < y[1]
	heap = Heap(graph[current_city], inequality)
	next_city = current_city
	while heap.size() > 0:
		next_city, path_cost = heap.pop()
		if next_city not in path:
			return next_city, path_cost
	return None



def TSP(graph, starting_city):
	path = [starting_city]
	cost = 0
	current_city = path[-1]
	while len(path) < len(graph):
		next_city, path_cost = calculate_next_city(graph, path, current_city)
		path.append(next_city)
		cost += path_cost
		current_city = path[-1]
	next_city, path_cost = find_my_way_back(graph, starting_city, current_city)
	path.append(next_city)
	cost += path_cost
	return path, cost


graph = {
	1: [(2,5), (3,8), (4,30)], # (city, cost)
	2: [(1,5), (3,9), (4,7)],
	3: [(1, 8), (2,9), (4, 6)],
	4: [(1, 3), (2,7), (3,6)]
}

def execute(graph, city):
	print("calculating TSP for {0}".format(city))
	print(TSP(graph, city))

execute(graph, 1)
execute(graph, 2)
execute(graph, 3)
execute(graph, 4)