def is_valid(n, x, y):
	# any other grid constrains can be modeled in this
	# method
	return (x<n and y < n)

def find_paths(count, n, x, y):
	if not is_valid(n, x, y):
		return
	if x==(n-1) and y==(n-1):
		count[0]+=1
		return
	find_paths(count, n, x+1, y)
	find_paths(count, n, x, y+1)


def count_paths(n):
	# passing the counter in an array to pass it as reference
	# to the recursive calls. In a class I would expect it to be
	# an instance variable
	count = [0]
	# making it zero indexed
	find_paths(count, n, 0, 0)
	return count[0]

print(count_paths(9))