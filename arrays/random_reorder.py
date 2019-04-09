# Taken from: https://www.youtube.com/watch?v=CoI4S7z1E1Y&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=11
# We have random.randrange(n) that has the same effect
# as a 0< floor(random)*n < 1
import random
# O(n)
def random_reorder(array):
	for i in range(len(array)-1, 0, -1):
		new_position = random.randrange(i)
		array[i], array[new_position] = array[new_position], array[i]
	return array

array = [1, 3, 9, 2]

print('random reorder of ', array)
print(random_reorder(array))