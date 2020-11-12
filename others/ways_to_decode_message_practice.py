# Asumming message containg digits only.
# O(n)
# In this case we would need to implement it with a hashmap as we dont want to store a vector full
# of 0's because most likely (assuming) the distribution for a given lenguage will be not uniformed
# distributed and a lot of combinations wont be used.
def ways_to_decode(message, code):
	sum = [0]
	dp_ways_to_decode(message, code, sum)
	return sum[0]

def dp_ways_to_decode(message, code, sum):
	if len(message) == 0:
	 	sum[0] +=1
	 	return
	if int(message[0]) not in code:
		return

	if len(message) > 1 and int(message[0:2]) in code:
		dp_ways_to_decode(message[2:], code, sum)
	dp_ways_to_decode(message[1:], code, sum)

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