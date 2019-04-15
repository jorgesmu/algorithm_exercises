def anagrams(s1, s2):
	if len(s1) != len(s2):
		return False
	for i in range(len(s1)):
		if s1[i] != s2[-i-1]:
			return False
	return True

def execute(s1, s2):
	print('s1: ', s1, ', s2: ', s2, ' anagrams: ', anagrams(s1, s2))

execute('banana', 'ananab')
execute('oso', 'oso')
execute('sfs', 'ananab')
execute('goloso', 'osolog')