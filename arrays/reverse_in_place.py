# Without swap variable
def reverse_no_swap(a):
	for i in range(int(len(a)/2)):
		a[len(a)-i-1] = a[len(a)-i-1] + a[i]
	
	for i in range(int(len(a)/2)):
		a[i] = a[len(a)-i-1] - a[i]

	for i in range(int(len(a)/2)):
		a[len(a)-i-1] = a[len(a)-i-1] - a[i]
	
# With swap
def reverse(a):
	for i in range(int(len(a)/2)):
		a[i], a[len(a)-i-1]= a[len(a)-i-1], a[i]

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print('array: ', a)
reverse_no_swap(a)
print('reverse no swap: ', a)

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
reverse(a)
print('reverse swap: ', a)