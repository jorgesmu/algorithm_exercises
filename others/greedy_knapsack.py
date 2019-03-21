def calculate_performance_and_sort(elements):
	for element in elements:
		element["performance"] = element["v"]/element["w"]
	return sorted(elements, key=lambda k: -k["performance"])

# This is considering 0-1 knapsack
# Cannot split elements into partial 
# amount of them.
# This is an heuristic fast approach O(n). That will lead to
# non optimal solutions in many cases. If we could divide the elements
# then this solution will be the perfect one. 
def knapsack(capacity, elements):
	sorted_elements = calculate_performance_and_sort(elements) 
	packed_elements = []
	for element in sorted_elements:
		if element["w"] < capacity:
			capacity -= element["w"]
			packed_elements.append(element)
	return packed_elements

elements = [
	{
		"w": 3, # wieght
		"v": 3, # value 
	},
	{
		"w": 5,
		"v": 2,
	},
	{
		"w": 4,
		"v": 2,
	},
	{
		"w": 6,
		"v": 3,
	},
	{
		"w": 2,
		"v": 3,
	},
	{
		"w": 1,
		"v": 1,
	},
	{
		"w": 7,
		"v": 3,
	},
	{
		"w": 2,
		"v": 1,
	},
	{
		"w": 0.3,
		"v": 0.002,
	},
]

print(knapsack(9, elements))