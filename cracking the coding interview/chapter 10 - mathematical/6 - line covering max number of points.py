def add_slope(lines, slope, intercept, p1, p2):
	if slope not in lines:
		lines[slope] = {}
	if intercept not in lines[slope]:
		lines[slope][intercept] = []
	if p1 not in lines[slope][intercept]:
		lines[slope][intercept].append(p1)
	if p2 not in lines[slope][intercept]:
		lines[slope][intercept].append(p2)


def max_line(lines):
	max_points = -1
	max_slope = None
	max_intercept = None
	points = None
	for slope in lines:
		for intercept in lines[slope]:
			if len(lines[slope][intercept]) > max_points:
				max_points = len(lines[slope][intercept])
				max_slope = slope
				max_intercept = intercept
	return max_slope, max_intercept, max_points


def optimal_line(points):
	lines = {}
	for i in range(len(points)):
		x1, y1 = p1 = points[i]
		for j in range(i+1, len(points)):
			x2, y2 = p2 = points[j]
			if x1 == x2:
				slope = 'vertical'
				# in this case intercept will be to the x axis not the y axis. Representing x=x1 line
				intercept = x1
			else:
				slope = (y2 - y1)/(x2 - x1)
				intercept = y1 - slope * x1 
				slope = round(slope, 2) # delta is 0.01
				intercept = round(intercept, 2)
			add_slope(lines, slope, intercept, p1, p2)
	return max_line(lines)
points = [(0,-60), (1,1), (2,2), (5,5), (10,10), (8,7), (2,65), (-7,1)]

print(optimal_line(points))