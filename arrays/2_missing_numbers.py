# Taken from: https://www.youtube.com/watch?v=75Jrba2uGFM

# Using O(n) in both space and memory usage.
# sorting would be n*log(n) but no extra space would be used
def missing(array, missing_count=2):
	viewed = set(array)
	missing = []
	i = 1
	while len(missing) < missing_count:
		if i not in viewed:
			missing.append(i)
		i+=1
	return missing

# from the video
def missing_one(array):
	expected_sum = 0
	for i in range(1, len(array)+2):
		expected_sum += i
	return expected_sum - sum(array)

def missing_one_bit_manipulation(array):
	expected_xor = actual_xor = 0
	for i in range(1, len(array)+2):
		expected_xor ^= i
	for i in array:
		actual_xor ^= i
	return expected_xor ^ actual_xor

def missing_bit_manipulation(array):
	expected_sum = 0
	for i in range(1, len(array)+3):
		expected_sum += i
	missing_sum = expected_sum - sum(array)

	# We know that one number is greater than missing/2 and one
	# will be greater as there are no repeats in the sequence
	middle = missing_sum / 2
	expected_lower_xor = lower_xor = 0
	expected_upper_xor = upper_xor = 0
	for i in range(1, len(array)+3):
		if i < middle:
			expected_lower_xor ^= i
		else:
			expected_upper_xor ^= i

	for i in array:
		if i < middle:
			lower_xor ^= i
		else:
			upper_xor ^= i

	return (expected_lower_xor ^ lower_xor), (expected_upper_xor ^ upper_xor)

array = [4, 2, 5, 6, 3]
print('missing for: ', array, ' is: ', missing(array))

array = [4, 2, 1, 6, 3]
print('missing one: ', array, ' is: ', missing_one(array))

array = [4, 2, 1, 6, 3]
print('missing one bit implementation: ', array, ' is: ', missing_one_bit_manipulation(array))

array = [4, 2, 5, 6, 3]
print('missing bit implementation for: ', array, ' is: ', missing_bit_manipulation(array))