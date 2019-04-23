# Taken from: https://www.youtube.com/watch?v=5LCuroQltsc&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=36
# long division: https://www.youtube.com/watch?v=rinhqaTwQnU
import math

def modulus(bytes_array, n):
	modulus = 0

	base_bits = 8
	for i in bytes_array:
		modulus = ((modulus<<base_bits) + i) % n
	return modulus

array = bytes.fromhex('deadbeef')
print('0x', array, ' modulus 14 is: ', modulus(array, 14))