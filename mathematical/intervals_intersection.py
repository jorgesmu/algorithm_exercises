# Given two intervals in a unidimensional space. Find the
# intersection interval between them. Each interval is
# represented by a start and end

def intersection(s1, e1, s2, e2):
	start = max(s1, s2)
	end = min(e1, e2)
	if end - start <= 0:
		return None, None
	return start, end


def execute(s1, e1, s2, e2):
	print('intersection of s1: ', s1, ' e1: ', e1, ' s2: ', s2, ' e2:', e2)
	print('is: ', intersection(s1, e1, s2, e2))

execute(2, 5, 3, 7)
execute(2, 5, 3, 70)
execute(3, 7, 3, 7)
execute(3, 5, 5, 7)
execute(3, 5, 4, 7)

