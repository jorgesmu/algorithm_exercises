# Complexity: O(nlogn)
def merge(collection1, collection2):
	sorted_items = []
	while(len(collection1) > 0 and len(collection2) > 0):
		if collection1[0] > collection2[0]:
			element = collection2.pop(0)
		else:
			element = collection1.pop(0)
		sorted_items.append(element)
	return sorted_items + collection1 + collection2

def mergesort(collection):
	collection_size = len(collection)
	if collection_size <= 1:
		return collection
	middle = int(collection_size/2)
	sorted_left = mergesort(collection[0:middle])
	sorted_right = mergesort(collection[middle:])
	return merge(sorted_left, sorted_right)

collection = [1, 3, 23, 42, -2, 1234, 6, 7, 6]
print(mergesort(collection))

