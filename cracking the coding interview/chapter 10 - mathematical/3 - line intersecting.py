# Assumptions: given two lines l1 and l2 if L1 is equal to L2 they intersec
# l1(x) = a1 x + b1
# l2(x) = a2 x + b2

# To check if they intersec we will need to find a point x that makes
# l1(x) = l2(x)
# a1 x + b1 = a2 x + b2
# E1: x = (b2-b1)/(a1 - a2)
# as we can see we are working in the cartesian plane with real numbers
# and as we see at E1 x will exist for every pair of lines except
# for the special case where a1 = a2 as we are dividing by zero and we need to
# analize this special case in isolation. 
# This was an expected result given that we are working on the full domain of
# the plane and if a pair of lines are not parallel, then we expect them to intersect at some point.

# Now lets analyze a1 = a2. This can happen on two situations:
# l1 = l2, in this case both lines intersec
# or l1 != l2 but they have equal pendient what means they are parallel lines and
# dont intersec

def intersec(a1, b1, a2, b2):
	if a1 != a2:
		return True
	if b1 == b2:
		return True
	return False

print("Parallel lines dont intersec:")
print(intersec(1, 0, 1, 1))

print("Same lines intersec:")
print(intersec(1, 1, 1, 1))

print("Not parallel lines  intersec:")
print(intersec(1, 0, 7, 1))