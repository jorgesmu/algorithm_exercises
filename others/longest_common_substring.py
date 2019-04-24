# Taken from: https://www.youtube.com/watch?v=aVFWW3pBQFo&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=22

# Time: O(s1*s2), space: O(s1*s2)
def lcs(s1, s2):
	result = ''
	if not s1 or not s2:
		return None
	if len(s1) == 0 or len(s2) == 0:
		return result
	cache = [[0 for col in range(len(s2))] for row in range(len(s1))]

	for row in range(len(s1)):
		for col in range(len(s2)):
			if s1[row] == s2[col]:
				import pdb; pdb.set_trace
				if row == 0 or col == 0:
					cache[row][col] = 1
				else:
					cache[row][col] = cache[row-1][col-1]+1

				if cache[row][col] > len(result):
					result = s1[row-len(result):row+1]
	return result
s1 = 'abab'
s2 = 'baba'
print('s1: ', s1)
print('s2: ', s2)
print('lcs is: ', lcs(s1, s2))