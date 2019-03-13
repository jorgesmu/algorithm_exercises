import operator
# notice that is min heap by deafult but can be max heap changing the operator
class Heap(object):
	def __init__(self, array, inequality = operator.lt):
		self.array = array
		self.inequality = inequality
		if len(array) == 0:
			return
		self.heapify()


	def push(self, element):
		self.array.append(element)
		self.sift_up()


	def pop(self):
		if len(self.array) == 0:
			return None
		self.array[0], self.array[len(self.array)-1] = self.array[len(self.array)-1], self.array[0]
		element = self.array.pop()
		# reestablish the heap condition
		if len(self.array) > 1 :
			self.sift_down(len(self.array)-1)

		return element
	

	def left_child(self, index):
		return 2*index + 1


	def right_child(self, index):
		return 2*index + 2


	def parent(self, index):
		if index <= 0:
			return None
		parent_index = int((index-1)/2)
		return parent_index


	# sift up the last element
	def sift_up(self):
		array = self.array
		if len(array) == 1:
			return
		current_index = len(array)-1
		parent_index = self.parent(current_index)
		while(parent_index is not None):
			if self.inequality(array[parent_index],  array[current_index]):
				return
			array[parent_index], array[current_index] = array[current_index], array[parent_index]
			current_index = parent_index
			parent_index = self.parent(current_index)


	# sift_down is log(n)
	def sift_down(self, max, current_index = 0):
		if max == 0:
			return
		left_index = self.left_child(current_index) 
		while(left_index <= max):
			swap_index = current_index
			if self.inequality(self.array[left_index], self.array[swap_index]):
				swap_index = left_index
			right_index = self.right_child(current_index)
			if right_index <= max and self.inequality(self.array[right_index], self.array[swap_index]):
				swap_index = right_index
			if swap_index == current_index:
				return
			self.array[swap_index], self.array[current_index] = self.array[current_index], self.array[swap_index]
			current_index = swap_index
			left_index = self.left_child(current_index)
		return


	def array(self):
		return self.array


	# Heapify is O(n)
	def heapify(self):
		max_index = len(self.array) - 1
		first_parent = self.parent(max_index)
		for i in range(first_parent, -1, -1):
			self.sift_down(max_index, i)
