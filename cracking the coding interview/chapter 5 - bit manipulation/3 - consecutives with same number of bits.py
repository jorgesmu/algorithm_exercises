def next(n):
	if n <= 1:
		raise Exception('Looking for positive integer > 1')
	ones_count = max_zero_position = 0
	bit_count = 0
	mask = 1<<bit_count
	while(mask<n*2): # multiplying by two because we want to find the next zero if ends in ones
		if (n&mask) > 0:
			ones_count+=1
		else:
			if ones_count > 0:
				max_zero_position = bit_count

		bit_count+=1
		mask = 1<<bit_count
	# substracting one from ones_count because its included in the max_zero_position
	return (1<<max_zero_position) + (1<<ones_count-1) - 1




print("Next of 011100, should be 100011")
print(bin(next(int('011100',2))))
# example: 
# n = 011100 
# next 100011