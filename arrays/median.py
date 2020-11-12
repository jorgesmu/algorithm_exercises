# Taken from: https://www.youtube.com/watch?v=HGgdcKbC5ro&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=53&t=1727s
import math
def median_helper(a1, s1, e1, a2, s2, e2):
	if e1 - s1 == 1:
		lower = min(a1[s1], a2[s2])
		upper = max(a1[e1], a2[e2])
		return (lower+upper)/2

	import pdb; pdb.set_trace()
	middle_element_a1 = s1 + (e1 - s1)/2
	middle_element_a2 = s2 + (e2 - s2)/2
	if (e1-s1)%2  == 0:
		med_a1 = a1[middle_element_a1]
		med_a2 = a2[middle_element_a2]
	else:
		med_a1 = (a1[math.floor(middle_element_a1)] + a1[math.ceil(middle_element_a1)])/2
		med_a2 = (a2[math.floor(middle_element_a2)] + a2[math.ceil(middle_element_a2)])/2
	if med_a1 == med_a2:
		return med_a1
	elif med_a1 > med_a2:
		return median_helper(a1, s1, math.ceil(middle_element_a1), a2, math.floor(middle_element_a2), e2)
	return median_helper(a1, math.floor(middle_element_a1), e1, a2, math.floor(middle_element_a2), e2)

def median(a1, a2):
	return median_helper(a1, 0, len(a1)-1, a2, 0, len(a2)-1)

a1 = [1, 2, 3, 4, 5, 6]
a2 = [0, 0, 0, 0, 10, 10]

print('a1: ', a1, ', a2: ', a2)
print('median: ', median(a1, a2))