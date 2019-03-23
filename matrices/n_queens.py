from copy import deepcopy
def print_board(board):
	for row in range(len(board)):
		print(board[row])

def valid_row(n, board, row, col):
	for ri in range(n):
		if board[ri][col] == True:
			return False
	return True

def valid_col(n, board, row, col):
	for ci in range(n):
		if board[row][ci] == True:
			return False
	return True
def valid(n, board, row, col):
	if not valid_row(n, board, row, col):
		return False

	if not valid_col(n, board, row, col):
		return False

	diagonal_row = row
	diagonal_col = col
	while diagonal_col >= 0 and diagonal_row >= 0:
		if board[diagonal_row][diagonal_col] == True:
			return False
		diagonal_col-=1
		diagonal_row-=1

	diagonal_row = row
	diagonal_col = col
	while diagonal_col >= 0 and diagonal_row < n:
		if board[diagonal_row][diagonal_col] == True:
			return False
		diagonal_col-=1
		diagonal_row+=1
	return True

# O(n^n)
def n_queens(n, ci, placed_queens, board, results):
	if placed_queens == n:
		results.append(board)
		return
	for row in range(n):
		if valid(n, board, row, ci):
			new_board = deepcopy(board)
			new_board[row][ci] = True
			n_queens(n, ci+1, placed_queens+1, new_board, results)
	return results

def perform_n_queens(n):
	board = [[False for i in range(n)] for i in range(n)]
	return n_queens(n, 0, 0, board, [])

print(len(perform_n_queens(4))) # we need to remove identical rotations of the board
