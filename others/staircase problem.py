# taken from: https://www.youtube.com/watch?v=5o-kdjv7FD0
# O(n*s), s = number of possible steps

def num_ways(n, steps):
	cache = [None for i in range(n+1)]
	return dynamic_num_ways(n, steps, cache)

def dynamic_num_ways(n, steps, cache):
	if cache[n]:
		return cache[n]

	if n == 0:
		return 1

	ways = 0
	for step in steps:
		if (n-step) >= 0:
			ways += num_ways(n-step, steps)

	cache[n] = ways
	return ways


print(num_ways(4, [1,2]))