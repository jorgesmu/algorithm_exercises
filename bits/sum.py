# https://www.youtube.com/watch?v=te4q1ivGons&list=PLNmW52ef0uwsMppECkGBpoao1p0_xWX2E&index=10

def sum(a,b):
	int_size = 32
	overflow = 0
	mask = 1
	current_sol = 0
	for i in range(1, int_size+1):
		if i > 1:
			mask <<= 1
		current_bit = (a&mask) ^ (b&mask) ^ overflow
		overflow = (((a&mask) & (b&mask)) | ((a&mask) & overflow) | ((b&mask) & overflow))<<1
		current_sol = current_sol | current_bit
	return current_sol

# Video implementation
def sum_v2(a, b):
	if b == 0:
		return a
	partial_sum = a^b
	overflow = (a&b) << 1
	return sum_v2(partial_sum, overflow)
	
a = 567
b = 456

print('a: ', a, ' , b: ', b)
print('sum = ', sum(a,b))