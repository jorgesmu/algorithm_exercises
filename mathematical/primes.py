import math

def primes_up_to(n):
	if n <= 1:
		return []
	primes = [2]
	for num in range(3, n+1, 2):
		divisor_found = False
		divisor = 3
		while divisor < (math.sqrt(n) + 1) and not divisor_found:
			if num % divisor == 0:
				divisor_found = True
			divisor += 1
		if not divisor_found:
			primes.append(num)
	return primes

print('Primes up to 1000')
print(primes_up_to(1000))
