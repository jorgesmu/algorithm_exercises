# Taken from: https://www.youtube.com/watch?v=bMF2fG9eY0A

# Time: O(n), Memory o(n) (in worse case O(n/2) but still ~O(n))
def find_num(a):
	odds = set()
	for num in a:
		if num in odds:
			odds.remove(num)
		else:
			odds.add(num)
	if len(odds) != 1:
		raise Exception('Precondition of only 1 number with odd number of repeats is not fulfilled')
	return odds.pop()


a = [4, 4, 4, 6, 4, 6, 6, 5, 5]
print('Array: ', a)
print('Number with odds repeats: ', find_num(a))