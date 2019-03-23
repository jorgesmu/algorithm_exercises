# Implementation based on https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def knapsack(w, vt, wt):
	values = [[None for ei in range(len(vt)+1)] for wi in range(w+1)] # values[capacity][element]
	for wi in range(w+1):
		for ei in range(len(vt)+1):
			if wi == 0 or ei == 0:
				values[wi][ei] = 0
			elif wt[ei-1] > wi:
				values[wi][ei] = values[wi][ei-1]
			else:
				skipping_obj = values[wi][ei-1]
				putting_obj = vt[ei-1] + values[wi-wt[ei-1]][ei-1]
				values[wi][ei] = max(skipping_obj, putting_obj)
	return values[w][len(vt)]

def recursive_knapsack(wi, ei, vt, wt, values):
	# import pdb; pdb.set_trace()
	if values[wi][ei] != None:
		return values[wi][ei]
	elif wi == 0 or ei == 0:
		value = 0
	elif wt[ei-1] > wi:
		value = recursive_knapsack(wi, ei-1, vt, wt, values)
	else:
		skipping_obj = recursive_knapsack(wi, ei-1, vt, wt, values)
		putting_obj = vt[ei-1] + recursive_knapsack(wi-wt[ei-1], ei-1, vt, wt, values)
		value = max(skipping_obj, putting_obj)
	values[wi][ei] = value
	return value
vt = [50, 60, 100, 120, 180] 
wt = [50, 10, 20, 30, 25] 
w = 50
print('Result with dynamic programing:')
print(knapsack(w, vt, wt))

# Recursive
values = [[None for ei in range(len(vt)+1)] for wi in range(w+1)] # values[capacity][element]
print('Result with dynamic programing recursive solution:')
print(recursive_knapsack(50, 5, vt, wt, values))
