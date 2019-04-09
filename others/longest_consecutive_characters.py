# taken from: https://www.youtube.com/watch?v=qRNB8CV3_LU&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=13&t=111s
# O(n)
def longest_consecutive_chars(string):
	longest_char = last_seen_char = None
	longest_repeat = current_repeat = 0

	for i in string:
		if i != last_seen_char:
			current_repeat = 1
			last_seen_char = i
		else:
			current_repeat+=1

		if current_repeat > longest_repeat:		
				longest_repeat = current_repeat
				longest_char = last_seen_char
	return { longest_char: longest_repeat }

string = 'AABCDDBBBEAA'
print(longest_consecutive_chars(string))