def calculate_center(square):
	starting_point, ending_point = square
	xs, ys = starting_point
	xe, ye = ending_point
	x = (xe + xs)/2
	y = (ys + ye)/2
	return x, y


def points_to_line(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	if x1 == x2:
		slope = 'vertical'
		# in this case intercept will be to the x axis not the y axis. Representing x=x1 line
		intercept = x1
	else:
		slope = (y2 - y1)/(x2 - x1)
		intercept = y1 - slope * x1 
		slope = round(slope, 2) # delta is 0.01
		intercept = round(intercept, 2)
	return slope, intercept


def generate_line(square1, square2):
	center1 = calculate_center(square1)
	center2 = calculate_center(square2)
	if square1 == square2:
		slope = 1	# From all the possible lines that pass through a point we choose the one with slope = 1
		intersect = center1[1] - center1[0]
		return slope, intersect
	return points_to_line(center1, center2)


# square ((xs,ys)(xe,ye)))
# assumtions: our data will came in this format
# each square will be defice by top left vertex
# and bottom right vertex.
# so xs < xe and ys > ye
square1 =((2,2), (4, 0))
square2 =((-1,1), (1, -1))

print(generate_line(square1, square2))