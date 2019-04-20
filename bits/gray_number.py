# taken from: https://www.youtube.com/watch?v=LqxtPV8xKeI&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=20

# a^b will give us a number with 1's in each position that
# is a and b differ
# Then we need to count how many 1's there are to ensure
# that only one position was changed.
# This is only possible if a^b == 2^n where n>=0
# we can check this by (c)&(c-1) == 0

# we are assuming that if a==b is_gray_number is false

def is_gray_number(a, b):
	if a == b:
		return False
	return ((a^b)&((a^b)-1) == 0)

def execute(a, b):
	print('a: ', a)
	print('b: ', b)
	print('is_gray_number: ', is_gray_number(a, b))

execute(0, 1)
execute(1, 1)
execute(1, 2)
execute(int('01010101010',2), int('01110101010',2))
execute(41, 12)
execute(41, 41)
