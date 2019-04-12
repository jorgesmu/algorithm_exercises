# Taken from: https://www.youtube.com/watch?v=VzQ2KacyDLw

# O(n) as we iterating over the array once
def move_zeros(a):
	back_pointer = len(a ) - 1
	i = 0
	while i < len(a) - 1 and i < back_pointer:
		if a[i] == 0:
			while back_pointer > i and a[back_pointer] == 0:
				back_pointer-=1
			a[i], a[back_pointer] = a[back_pointer], a[i]
		i+=1
	return

a = [1, 0, 0, 0, 0]
print('move zeros for: ', a)
move_zeros(a)
print('is: ', a)

a = [0, 0, 0, 1, 0, 0]
print('move zeros for: ', a)
move_zeros(a)
print('is: ', a)

a = [0, 0, 0, 4, 0, 6]
print('move zeros for: ', a)
move_zeros(a)
print('is: ', a)

a = [10, 0, 20, 4, 0, 0, 6, 0]
print('move zeros for: ', a)
move_zeros(a)
print('is: ', a)
