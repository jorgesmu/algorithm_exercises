# Problem taken from: https://www.youtube.com/watch?v=Qf5R-uYQRPk&index=4&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD&t=0s

def lcs(p, q, pi, qi):
	if pi == -1 or qi == -1:
		return 0
	if p[pi] == q[qi]:
		return 1 + lcs(p, q, pi-1, qi-1)
	else:
		return max(lcs(p, q, pi, qi-1), lcs(p, q, pi-1, qi))


p = 'baterd'
pi = len(p) - 1
q = 'abaercd'
qi = len(q) - 1
print(lcs(p, q, pi, qi))