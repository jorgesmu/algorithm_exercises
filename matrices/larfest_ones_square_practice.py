# Taken from: https://www.youtube.com/channel/UCYvQTh9aUgPZmVH0wNHFa1A
import random

# O(n) + O(n) in space
def count(matrix):
	max = 0
	cache = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 1:
				if row == 0 or col == 0:
					cache[row][col] = matrix[row][col]
				else:
					cache[row][col] = matrix[row][col] + min(cache[row-1][col], cache[row][col-1], cache[row-1][col-1])
				if cache[row][col] > max:
					max = cache[row][col]
	return max
rows = 7
cols = 7
matrix = [[random.randrange(2) for i in range(cols)] for j in range(rows)]
for row in matrix:
	print(row)
print('largest 1\'s square: ', count(matrix))
