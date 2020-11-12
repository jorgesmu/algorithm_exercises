from copy import deepcopy
def is_valid(n, col, row, board):
	if col == 0:
		return True
	for i in range(col):
		if board[row][i] == True:
			return False
	# y = ax + b
	# y = x + b
	# b =  y -x

	# y = -ax + b
	# y = -x + b
	# b =  y +x
	# y = -x +2
	b_pos = row - col
	b_neg = row + col
	for i in range(col):
		current_row = i + b_pos
		if current_row >= 0 and current_row < n:
			if board[current_row][i] == True:
				return False
	for i in range(col):
		current_row = -i + b_neg
		if current_row >= 0 and current_row < n:
			if board[current_row][i] == True:
				return False
	return True
def n_queens(n, col, board, res):
	if col >= n:
		res[0]+=1
		return
	for row in range(n):
		if is_valid(n, col, row, board):
			board[row][col] = True
			n_queens(n, col+1, board, res)
			board[row][col] = False
	return res[0]

def perform_n_queens(n):
	res = [0]
	board = [[False for i in range(n)] for i in range(n)]
	return n_queens(n, 0, board, res)


print(perform_n_queens(8))# we need to remove identical rotations of the board)