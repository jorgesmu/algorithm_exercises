# squares mechanism
# https://www.youtube.com/watch?v=hVl2b3bLzBw
from math import ceil
def merge(a, l, m, r):
	square_size = ceil((r - l)/2)
	ones = False
	while square_size >= 1 and not ones:
		if square_size == 1:
			ones = True
		i=l
		j=i+square_size

		while j <= r:
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
			i+=1
			j+=1
		square_size = ceil(square_size/2)
	return
	

def rec_div(a, l, r):
	mid = (l+r)//2

	if (r - l) <= 0:
		return

	rec_div(a, l, mid)
	rec_div(a, mid + 1, r)

	return merge(a, l, mid, r)

def mergesort(a):
	rec_div(a, 0 , len(a)-1)
	return a

a = [56,34,2,6,0,99999,3,5,6, -1234]
mergesort(a)