# taken from: https://www.youtube.com/watch?v=lf2w3C82jYA&list=PLNmW52ef0uws098xXRbALoadgcc4bNkDm&index=6

def max_prod(matrix):
	rows = len(matrix)
	cols = len(matrix[0])

	max_prod = [[0 for i in range(cols)] for j in range(rows)]
	min_prod = [[0 for i in range(cols)] for j in range(rows)]
	max_prod[0][0] = min_prod[0][0] = matrix[0][0]

	for col in range(1, cols):
		max_prod[0][col] = matrix[0][col]*max_prod[0][col-1]
		min_prod[0][col] = matrix[0][col]*min_prod[0][col-1]

	for row in range(1, rows):
		max_prod[row][0] = matrix[row][0]*max_prod[row-1][0]
		min_prod[row][0] = matrix[row][0]*min_prod[row-1][0]

	for col in range(1, cols):
		for row in range(1, rows):
			max_prod[row][col] = max(matrix[row][col]*max_prod[row-1][col],
									matrix[row][col]*max_prod[row][col-1],
									matrix[row][col]*min_prod[row-1][col],
									matrix[row][col]*min_prod[row][col-1])
			min_prod[row][col] = min(matrix[row][col]*max_prod[row-1][col],
									matrix[row][col]*max_prod[row][col-1],
									matrix[row][col]*min_prod[row-1][col],
								 	matrix[row][col]*min_prod[row][col-1])
	return max_prod[rows-1][cols-1]
m1 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

m2 = [
	[-1, 2, 3],
	[4, 5, -6],
	[7, 8, 9],
]

print(max_prod(m2))