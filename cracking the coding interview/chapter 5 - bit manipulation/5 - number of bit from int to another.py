# Asumming its for natural numbers only
def bits_difference(a,b):
	if a == b or a < 0 or b < 0: 
		raise Exception('Unexpected input')
	xor = a ^ b
	ones = 0
	mask = 1
	while(mask<=xor):
		if mask&xor>0:
			ones+=1
		mask = mask<<1
	return ones

print('Bits shift between 31 and 14 is:')
print(bits_difference(31, 14))