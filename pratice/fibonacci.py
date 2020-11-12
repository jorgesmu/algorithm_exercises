def fib_helper(n, cache):
	if cache[n] is not None:
		return cache[n]
	cache[n] = fib_helper(n-1, cache) + fib_helper(n-2, cache)
	return cache[n]


def fib(n):
	#1
	# if n == 0:
	# 	return 0
	# if n == 1:
	# 	return 1
	# return fib(n-1) + fib(n-2)

	#2
	# if n == 0:
	# 	return 0
	# if n == 1:
	# 	return 1
	# first  = 1
	# second = 1
	# count = 2
	# while count < n:
	# 	new_term = first + second
	# 	first = second
	# 	second = new_term
	# 	count+=1
	# return second

	#3 
	if n == 0:
		return 0
	if n == 1:
		return 1
	cache = [None for i in range(n+1)]
	cache[0] = 0
	cache[1] = 1
	return fib_helper(n, cache)
for i in range(100):
	print(fib(i))