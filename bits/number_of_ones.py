# Taken from: https://www.youtube.com/watch?v=8iWIpkFgZ64&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=4

# Assuming n is positive and int
# O(log n)
def count_ones(num):
	ones = 0
	while(num>0):
		# import pdb; pdb.set_trace()
		ones+= num & 1
		num>>=1
	return ones
print(count_ones(7))
for i in range(50):
	print(i, ': ', count_ones(i))