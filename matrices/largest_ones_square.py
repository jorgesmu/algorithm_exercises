# Taken from: https://www.youtube.com/channel/UCYvQTh9aUgPZmVH0wNHFa1A
import random

def ones_count(counting_matrix, row, col):
	if (row - 1) < 0 or (col-1) < 0:
		return 1
	count_until_now = min(counting_matrix[row][col-1], counting_matrix[row-1][col], counting_matrix[row-1][col-1])
	return count_until_now + 1

# O(n) + O(n) in space
def count(matrix):
	counting_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	max = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 1:
				counting_matrix[row][col] = ones_count(counting_matrix, row, col)
				if counting_matrix[row][col] > max:
					max = counting_matrix[row][col]
	return max


rows = 10
cols = 10
matrix = [[random.randrange(2) for i in range(cols)] for j in range(rows)]
for row in matrix:
	print(row)
print('largest 1\'s square: ', count(matrix))
