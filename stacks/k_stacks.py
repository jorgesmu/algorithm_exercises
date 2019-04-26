# Taken from: https://www.youtube.com/watch?v=DxW7VAsdX0o&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=12
class Node:
	def __init__(self):
		self.previous = self.next = self.value = None

# This is a linked list approach as after we create
# the nodes in the array we dont really need them after all
# I see this implementation easier than maintaining multiple
# arrays to keep the pointers
class KStacks:
	def __init__(self, n, size_array):
		array = [Node() for i in range(size_array)]
		for i in range(len(array)):
			if i < len(array) -1:
				array[i].next = array[i+1]
			if i > 0:
				array[i].previous = array[i-1]
		self.free_list = array[0]
		self.pointers = [None for i in range(n)]

	def push(self, stack, element):
		if not self.free_list:
			raise Exception('out of space')
		node = self.free_list
		self.free_list = self.free_list.next
		node.value = element
		if self.pointers[stack]:
			self.pointers[stack].next = node
			node.previous = self.pointers[stack]
			self.pointers[stack] = self.pointers[stack].next
		else:
			self.pointers[stack] = node

	def pop(self, stack):
		if not self.pointers[stack]:
			raise Exception('No more elements in the stack')
		element = self.pointers[stack]
		self.pointers[stack] = self.pointers[stack].previous

		value = element.value
		element.value = None

		if self.free_list:
			element.next = self.free_list 
			self.free_list = element
		else:
			self.free_list = element
		return value

