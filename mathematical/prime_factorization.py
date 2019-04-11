# https://www.youtube.com/watch?v=6PDtgHhpCHo

def prime_factors(n):
	if n <= 1:
		return None
	factors = {}
	for i in range(2, n+1):
		if n%i == 0:
			factors[i] = 0
			while n%i == 0:
				factors[i]+=1
				n = n/i
	return factors

print('prime_factorization 700: ', prime_factors(700))
print('prime_factorization 34: ', prime_factors(34))
print('prime_factorization 1361: ', prime_factors(1361))
print('prime_factorization 70023452: ', prime_factors(70023452))