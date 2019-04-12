# Given two intervals in a unidimensional space. Find the
# intersection interval between them. Each interval is
# represented by a start and end

def intersection(s1, e1, s2, e2):
	start = end = None
	if not ((s1 >= s2 and s1 <= e2) or (s2 >= s1 and s2 <= e1) and (e1 != s2 and e2!= s1)):
		return start, end

	if s1 >= s2 and s1 <= e1:
		start = s1
	else:
		start = s2

	if e1 > s2 and e1 < e2:
		end = e1
	else:
		end = e2
	return start, end


def execute(s1, e1, s2, e2):
	print('intersection of s1: ', s1, ' e1: ', e1, ' s2: ', s2, ' e2:', e2)
	print('is: ', intersection(s1, e1, s2, e2))

execute(2, 5, 3, 7)
execute(2, 5, 3, 70)
execute(3, 7, 3, 7)
execute(3, 5, 5, 7)
execute(3, 5, 4, 7)

