# merge sort with extra space
def merge(b, c):
	res = []
	i = j = 0
	while i < len(b) and j < len(c):
		if b[i] < c[j]:
			res.append(b[i])
			i+=1
		else:
			res.append(c[j])
			j+=1

	while i < len(b):
		res.append(b[i])
		i+=1

	while j < len(c):
		res.append(c[j])
		j+=1
	return res

def rec_div(a, l, r):
	mid = (l+r)//2

	if (r - l) <= 0:
		return [a[l]]

	left_sorted = rec_div(a, l, mid)
	right_sorted = rec_div(a, mid + 1, r)

	
	return merge(left_sorted, right_sorted)

def mergesort(a):
	return rec_div(a, 0 , len(a)-1)

mergesort(a)