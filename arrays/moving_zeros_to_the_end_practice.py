def move(array):
	lead = 0
	follower = lead +1
	while lead < len(array) and follower < len(array):
		if array[lead] == 0:
			while follower < len(array) and array[follower] == 0:
				follower+=1
			if follower < len(array):
				array[lead], array[follower] = array[follower], array[lead]
		lead+=1
	return array
print(move([0,1,0,3,12]))
			# l f   l 