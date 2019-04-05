import random

def recursive_paint(image, height, width, target_color, color, x, y):
	if x < 0 or y < 0 or x >= width or y>= height or target_color != image[x][y]:
		return
	image[x][y] = color
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if i != x or j != y:
				recursive_paint(image, height, width, target_color, color, i, j)

# Paint fill in every direction including diagonals
# O(n) in the worst case
def paint_fill(image, height, width, color, x, y):
	target_color = image[x][y]
	recursive_paint(image, height, width, target_color, color, x, y)

height = 10
width = 10

# 3 colors representation
image = [[random.randrange(3) for i in range(height)] for j in range(width)]

def print_image(image):
	for row in image:
		print(row)

print_image(image)
color = random.randrange(3)
print('painting pixel 0,0 with color', color)
paint_fill(image, height, width, color, 0, 0)
print_image(image)
