# Taken from: https://www.youtube.com/watch?v=bK7BCWICvpQ&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=29

def bin_search_row(matrix, n, start, end):
	middle = int((start + end)/2)
	if middle == len(matrix)-1 or (matrix[middle][0] <= n and matrix[middle+1][0] > n):
		return middle
	if  matrix[middle][0] < n:
		return bin_search_row(matrix, n, middle+1, end)
	return bin_search_row(matrix, n, start, middle - 1)

def binary_search(array, n, start, end):
	middle = int((start + end)/2)
	if array[middle] == n:
		return True
	if start >= end:
		return False
	if array[middle] < n:
		return binary_search(array, n, middle+1, end)
	return binary_search(array, n, start, middle-1)

# O(log(rows) + log(cols))
def search(matrix, n):
	column = bin_search_row(matrix, n, 0, len(matrix) -1)
	return binary_search(matrix[column], n, 0, len(matrix[column])-1)

matrix = [[0, 2, 4, 6],
		  [8, 10, 12, 14],
		  [16, 18, 20, 22],
		  [24, 26, 28, 30]
]


def execute(n):
	print('looking for: ', n, ' found: ', search(matrix, n))

for i in range(40):
	execute(i)