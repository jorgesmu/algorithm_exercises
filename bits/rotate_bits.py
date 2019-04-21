# Taken from: https://www.youtube.com/watch?v=uDqUb50Bmvs&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=15

# rotating to the left
# Assuming 8 bits word
# O(rotations)
def rotate_iterative(num, rotations):
	word_size = 4
	mask = (1 << word_size) - 1 
	while rotations > 0:
		activated_bit = ((1 << (word_size-1)) & num) > 0
		num = ((num << 1) & mask) + activated_bit
		rotations -= 1
	return num


print('11 rotate_iterative 5 times on word size of 4 bits: ', bin(rotate_iterative(3, 5)))

def rotate(num, rotations):
	word_size = 4
	if rotations >= word_size:
		raise exception('invalid number of rotations')
	mask = (1 << word_size) - 1 
	num = ((num << rotations) & mask) | (num >> (word_size - rotations))

print('11 rotate 3 times on word size of 4 bits: ', bin(rotate_iterative(3, 3))) 