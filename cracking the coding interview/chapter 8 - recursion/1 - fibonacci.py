def fibonacci(n):
	if n <= 0:
		raise Exception('Trying to calculate an invalid fibonacci')
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))