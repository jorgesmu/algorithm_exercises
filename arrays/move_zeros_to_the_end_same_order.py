def move(array):
	last_position = pointer = 0

	while pointer < len(array):
		if array[pointer] != 0:
			array[last_position] = array[pointer]
			last_position+=1
		pointer+=1
	while last_position < len(array):
		array[last_position] = 0
		last_position+=1
	return array

print(move([0,1,0,3,12]))