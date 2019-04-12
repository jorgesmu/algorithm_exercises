# Taken from: https://www.youtube.com/watch?v=4HfDrisG3MQ

def in_danger(xk, yk, xq, yq):
	for i in [xk, yk, xq, yq]:
		if i < 1 or i > 8:
			raise Exception('Coordinate out of range')

	if xk ==  xq or yk == yq:
		return True

	# In order to be in the same diagonal there are two
	# possible lines that can go throgh the points.
	# In order to share the diagonal in the chess board
	# the slope of these need to be either 1 or -1
	# so will calculate the line for one of this coordinates
	# given the slope and will check later if the second
	# coordinate is in the same line

	b_pos = xk - yk
	b_neg = xk + yk
	if (xq + b_pos) == yq or (b_neg - xq) == yq:
		return True
	return False

xk = 1; yk = 1; xq = 2; yq = 2
print('points xk: ', xk, ' yk: ', yk, ' xq: ', xq, ' yq: ', yq)
print(in_danger(xk, yk, xq, yq))

xk = 1; yk = 1; xq = 2; yq = 3
print('points xk: ', xk, ' yk: ', yk, ' xq: ', xq, ' yq: ', yq)
print(in_danger(xk, yk, xq, yq))

xk = 4; yk = 5; xq = 5; yq = 4
print('points xk: ', xk, ' yk: ', yk, ' xq: ', xq, ' yq: ', yq)
print(in_danger(xk, yk, xq, yq))