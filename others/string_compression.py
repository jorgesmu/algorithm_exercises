# taken from: https://www.youtube.com/watch?v=XMKMgzU1uiw&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=8

def compress(string):
	output = ''
	freq = 0
	last_seen_char = None

	for i in string:
		if freq > 0 and last_seen_char != i:
			if last_seen_char:
				output += last_seen_char + str(freq)
			last_seen_char = i
			freq = 0
		freq+=1
	if last_seen_char:
		output += last_seen_char + str(freq)		
	return output

def execute(string):
	print('compress for: ', string, ' is: ', compress(string))

execute('a')
execute('aaa')
execute('aaaabbbbb')
execute('aaaabcdderee')
