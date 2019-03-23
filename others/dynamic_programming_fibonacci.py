# returns the n's term of fibonaccis sequence
# n is zero based
def perform_fibonacci(values, n):
	if values[n] is not None:
		return values[n]
	if n < 2:
		return n
	values[n] = perform_fibonacci(values, n-1) + perform_fibonacci(values, n-2)
	return values[n]

def fibonacci(n):
	values = [None for i in range(n+1)]
	return perform_fibonacci(values, n)
print(fibonacci(15))