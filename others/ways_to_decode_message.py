# Asumming message containg digits only.
# O(n)
# In this case we would need to implement it with a hashmap as we dont want to store a vector full
# of 0's because most likely (assuming) the distribution for a given lenguage will be not uniformed
# distributed and a lot of combinations wont be used.
def ways_to_decode(message, code):
	cache = [None for i in range(len(message)+1)]
	return dp_ways_to_decode(message, 0, code, cache)

def dp_ways_to_decode(message, k, code, cache):
	if k > len(message):
		return 0
		
	if k == len(message):
		return 1

	if cache[k]:
		return cache[k]

	if not int(message[k]) in code:
		return 0

	result = dp_ways_to_decode(message, k+1, code, cache)
	if len(message) > 1 and int(message[k:k+2]) in code:
		result += dp_ways_to_decode(message, k+2, code, cache)

	cache[k] = result
	return  result

code = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e',
	6: 'f',
	7: 'g',
	8: 'h',
	9: 'i',
	10: 'j',
	11: 'k',
	12: 'l',
	13: 'm',
	14: 'n',
	15: 'o',
	16: 'p',
	17: 'q',
	18: 'r',
	19: 's',
	20: 't',
	21: 'u',
	22: 'v',
	23: 'w',
	24: 'x',
	25: 'y',
	26: 'z'
}
message = "12"
print('ways of decode message: ', message, ' : ', ways_to_decode(message, code))

message = "01"
print('ways of decode message: ', message, ' : ', ways_to_decode(message, code))

message = "12564"
print('ways of decode message: ', message, ' : ', ways_to_decode(message, code))

message = "112413241342"
print('ways of decode message: ', message, ' : ', ways_to_decode(message, code))

message = "1124130000241342"
print('ways of decode message: ', message, ' : ', ways_to_decode(message, code))