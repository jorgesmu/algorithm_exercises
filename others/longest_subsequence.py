# Problem taken from: https://www.youtube.com/watch?v=Qf5R-uYQRPk&index=4&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD&t=0s
# O(pq)
def lcs(p, q, pi, qi, cache):
	if cache[qi][pi]:
		return cache[qi][pi]
	if pi == 0 or qi == 0:
		result = 0
	elif p[pi-1] == q[qi-1]:
		result =  1 + lcs(p, q, pi-1, qi-1, cache)
	else:
		result = max(lcs(p, q, pi, qi-1, cache), lcs(p, q, pi-1, qi, cache))
	cache[qi][pi] = result
	return result

p = 'baterd'
pi = len(p)
q = 'abaercd'
qi = len(q)
cache = [[None for i in range(len(p)+1)] for j in range(len(q)+1)]
print(lcs(p, q, pi, qi, cache))