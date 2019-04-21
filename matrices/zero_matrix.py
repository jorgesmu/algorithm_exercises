# Taken from: https://www.youtube.com/watch?v=ZzpJgRvqSJQ&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=43&t=22s

def activate_row(matrix, row):
	for col in range(len(matrix[0])):
		matrix[row][col] = True

def activate_col(matrix, col):
	for row in matrix:
		row[col] = True

def check_first_row(matrix):
	for row in matrix:
		if row[0] == True:
			return True
	return False

def check_first_col(matrix):
	for col in range(len(matrix[0])):
		if matrix[0][col] == True:
			return True
	return False

# O(n^2)
def mutate(matrix):
	if len(matrix) == 0 or len(matrix[0]) == 0:
		return

	row_zero_active = check_first_row
	col_zero_active = check_first_col

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == True:
				matrix[0][col] = True
				matrix[row][0] = True
	
	for row in range(1, len(matrix)):
		if matrix[row][0]:
			activate_row(matrix, row)
	
	for col in range(1, len(matrix[0])):
		if matrix[0][col]:
			activate_col(matrix, col)

	if row_zero_active:
		activate_row(matrix, 0)

	if col_zero_active:
		activate_col(matrix, 0)

rows = cols = 5

matrix = [[False for i in range(cols)] for j in range(rows)]
matrix[2][2] = True
matrix[0][0] = True

def print_matrix(matrix):
	for i in matrix:
		print(i)
print_matrix(matrix)
print('after_mutate:')
mutate(matrix)
print_matrix(matrix)