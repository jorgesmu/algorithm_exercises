from linked_list import Node

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

def lead_follower(li, n):
	# 1 2 3 4 5

	count = 0
	lead = li
	while count<n:
		lead = lead.next
		count+=1

	current = li
	while lead:
		lead = lead.next
		current = current.next
	return current.value

print('n = e using lead follower')
print(lead_follower(n1, 3))