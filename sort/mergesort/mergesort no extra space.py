# merge sort with O(r)*(O(n))merging time, no extra space
# https://www.youtube.com/watch?v=hVl2b3bLzBw
def merge(a, l, m, r):
	i = l
	

	while i < m+1:
		if a[m+1] < a[i]:
			a[i], a[m+1] = a[m+1], a[i]
			j = m+1
			while j < r and a[j]> a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				j+=1
		i+=1

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