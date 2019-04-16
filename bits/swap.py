# Taken from: https://www.youtube.com/watch?v=DtnH3V_Vjek&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=30

a = 6 
b = 5 

# Note that we are not really swapping as ints are inmutable
# and are passed by value to the swap function
def swap(a, b):
	a = a + b
	b = a - b
	a = a - b	
	return a, b

print('swap of a: ', a, ', b: ', b, 'is:')
a, b = swap(a, b)
print('a: ', a, ', b: ', b)

def swap_bits(a, b):
	a = a^b 
	b = a^b
	a = a^b
	return a, b

print('swap (bits implementation) of a: ', a, ', b: ', b, 'is:')
a, b = swap_bits(a, b)
print('a: ', a, ', b: ', b)	