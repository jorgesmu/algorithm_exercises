class CircularQueue:
	def __init__(self, size):
		self.array = [None for i in range(size)]
		self.front = self.rear = -1

	def queue(self, element):
		next_position = self.next_element(self.rear)
		if next_position == self.front:
			raise Exception('Queue run out of space')
		self.rear = next_position
		self.array[self.rear] = element
		if self.front == -1:
			self.front = 0


	def deque(self):
		if self.front == -1:
			raise Exception('No elements on the queue')
		element = self.array[self.front]
		if self.front == self.rear:
			self.front = self.rear = -1
		else:
			self.front = self.next_element(self.front)
		return element
		
	def next_element(self, index):
		if (index + 1) < len(self.array):
			return index + 1
		return 0