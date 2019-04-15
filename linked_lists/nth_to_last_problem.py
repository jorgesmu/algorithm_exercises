from linked_list import Node

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print('List: [1, 2, 3, 4, 5]')
# This is O(n), iterating the list twice
def not_extra_space(list, n):
	count = 0
	l1 = list
	while l1:
		count+=1
		l1 = l1.next

	if n >= count:
		return None
	
	looked_index = count - n - 1 # Zero based
	count = 0
	l1 = list
	
	while True:
		if count == looked_index:
			return l1.value
		count+=1
		l1 = l1.next

print('n = 3 using no extra space')
print(not_extra_space(n1, 3))

def recursive_approach(li, n):
	if li == None:
		return False, -1

	found, next_index =  recursive_approach(li.next, n)
	current_index = next_index + 1
	if not found and current_index == n:
		return True, li.value
	if found:
		return found, next_index
	return False, current_index

def n_last_recursive(l, n):
	found, value = recursive_approach(l, n)
	if not found:
		return None
	return value

print('n = 2 using recursion')
print(n_last_recursive(n1, 2))

# O(n)
def lead_follower(li, n):
	lead = 0
	lead_list = follower_list = li
	for i in range(n):
		if not lead_list.next:
			return None
		lead_list = lead_list.next


	while lead_list.next:
		lead_list = lead_list.next
		follower_list = follower_list.next
	return follower_list.value

print('n = e using lead follower')
print(lead_follower(n1, 3))