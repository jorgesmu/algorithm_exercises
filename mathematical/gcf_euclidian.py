# example: https://www.youtube.com/watch?v=cOwyHTiW4KE
# Demostration:
import math

def gcf(a, b):
	if b == 0:
		return a
	q = math.floor(a/b)
	r = a - q*b
	return gcf(b, r)

print('gcf 2328989892, 6234354 = ', gcf(2328989892, 6234354))