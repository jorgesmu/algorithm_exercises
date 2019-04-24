# taken from: https://www.youtube.com/watch?v=HlBG2O8ydhw&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=9

# time: O(nlog n)space: O(n)
def kth_most_frequent(words, k):
	if k > len(words):
		return None

	frequencies = {}
	for word in words:
		if word in frequencies:
			frequencies[word] += 1
		else:
			frequencies[word] = 1

	if k >= len(frequencies):
		return None

	frequencies = sorted(frequencies.items(), key=lambda x:x[1])
	return frequencies[k-1][0]

array = ['k', 'b', 'a' , 'b', 'c', 'a', 'a', 'b', 'd', 'b']
print('array: ', array)
for i in range(10):
	print(i, 'th most frequent: ', kth_most_frequent(array, i))