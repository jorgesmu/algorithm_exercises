# taken from: https://www.youtube.com/watch?v=rZ9lcXCWSUg&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=18

# O(n) in time, O(1) in space
# assuming a1 is always containing enough zeros for containing b
# and we are merging on a

# Given that the zeros are at the back we are merging backwards
def merge(a, b):
	placed_elements = 0 
	a_pointer =  len(a) - len(b) - 1
	b_pointer = len(b) - 1
	while a_pointer >= 0 and b_pointer >= 0:
		element_to_place = a[a_pointer]
		if a[a_pointer] < b[b_pointer]:
			a[-(1+placed_elements)] = b[b_pointer]
			b_pointer-=1
		else:
			a[-(1+placed_elements)] = a[a_pointer]
			a_pointer-=1
		placed_elements+=1

	while b_pointer >= 0:
		a[-(1+placed_elements)] = b[b_pointer]
		b_pointer-=1
		placed_elements+=1
	return





a = [1, 3, 5, 0, 0, 0, 0]
b = [-1, 2, 4, 6]

print('a: ', a)
print('b: ', b)
merge(a, b)
print(a)