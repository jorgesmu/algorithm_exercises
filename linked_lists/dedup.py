from linked_list import Node

# O(n^2)
def dedup_cuadratic(list):
	pointer = list
	while pointer:
		sub_pointer = pointer
		while sub_pointer.next:
			if sub_pointer.next.value == pointer.value:
				sub_pointer.next = sub_pointer.next.next
			else:
				sub_pointer = sub_pointer.next
		pointer = pointer.next
	return

n5 = Node(1)
n4 = Node(2, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

def print_list(list):
	while list:
		print(list.value)
		list = list.next

print('dedup_cuadratic for 1 -> 2 -> 3 -> 2 -> 1')
dedup_cuadratic(n1)
print_list(n1)

n5 = Node(1)
n4 = Node(2, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

# Time: O(n) space: O(n)
def dedup_with_memory(list):
	viewed = set()
	pointer = list
	while pointer:
		viewed.add(pointer.value)
		if pointer.next and pointer.next.value in viewed:
			if pointer.next.next:
				pointer.next = pointer.next.next
			else:
				pointer.next = None
		else:
			pointer = pointer.next
	return

print('dedup_with_memory for 1 -> 2 -> 3 -> 2 -> 1')
dedup_with_memory(n1)
print_list(n1)