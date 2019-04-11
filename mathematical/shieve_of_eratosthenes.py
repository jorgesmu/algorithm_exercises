def shieve_of_eratosthenes(n):
	criba = [True for i in range(n+1)]
	criba[0] = criba[1] = False
	primes = []
	for i in range(2, n+1):
		if criba[i]:
			primes.append(i)
			j = 2*i
			while j <= n:
				criba[j] = False
				j += i
	return primes

print('shieve_of_eratosthenes up to 100:')
print(shieve_of_eratosthenes(100))