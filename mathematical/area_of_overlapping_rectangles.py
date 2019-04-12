# Taken from: https://www.youtube.com/watch?v=zGv3hOORxh0&t=30s
from  intervals_intersection import intersection

def intersection_area(r1, r2):
	lx1, ly1 = r1[0] # lx = left x, ly = left y
	rx1, ry1 = r1[1] # rx = right x, ry = right y

	lx2, ly2 = r2[0]
	rx2, ry2 = r2[1]

	x_intersection = intersection(lx1, rx1, lx2, rx2)
	y_intersection = intersection(ly1, ry1, ly2, ry2)

	if not x_intersection or not y_intersection:
		return 0
	x_intersection_length = x_intersection[1] - x_intersection[0]
	y_intersection_length = y_intersection[1] - y_intersection[0]

	return x_intersection_length * y_intersection_length

def execute(r1, r2):
	print('r1: ', r1)
	print('r2: ', r2)
	print('intersection area: ', intersection_area(r1, r2))

rect1 = ((2,1), (5,5))
rect2 = ((3,2), (5,7))
execute(rect1, rect2)

rect1 = ((-1,1), (15,5))
rect2 = ((3,2), (7,7))
execute(rect1, rect2)