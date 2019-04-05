def calculate(n, m, i, j):
	left_mask = (1 << i) - 1
	right_mask = (2**(31-j) - 1) << j+1
	mask = right_mask + left_mask # mask with all 1 except between i and j
	turned_off_n = n & mask # turn off all bits between i and j
	shifted_m = m << i
	return  turned_off_n | shifted_m
	

n = int('10000000000',2)
m = int('10101',2)
res = int('10001010100',2)
i = 2
j = 6


print('m=10000000000, n=10101, i=2, j=6')
print('expected result: ', res)
print('actual result: ', calculate(n,m,i,j))
