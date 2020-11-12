def empty_slots(seen, starting, k):
	if starting < 0:
		return False
	for i in range(starting, starting + k):
		if i in seen:
			return False
	return True

def kEmptySlots(flowers, k):
	if len(flowers) == 0:
		return -1
	seen = set()
	seen.add(flowers[0])
	for i in range(1, len(flowers)):
		import pdb; pdb.set_trace()
		seen.add(flowers[i])
		if ((flowers[i]-k-1) in seen and empty_slots(seen, flowers[i]-k, k)) or ((flowers[i]+k+1) in seen and empty_slots(seen, flowers[i]+1, k)):
			return i+1
	return -1

print(kEmptySlots([6,5,8,9,7,1,10,2,3,4], 2))