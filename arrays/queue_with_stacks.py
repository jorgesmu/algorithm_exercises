# Implement a queue using stacks.
# A different solution of this problem: https://www.youtube.com/watch?v=71kEvXsEKYQ

from stack import Stack

class Queue:
	def __init__(self):
		self.enqueue_stack = Stack()
		self.dequeue_stack = Stack()

	def size(self):
		return self.enqueue_stack.size() + self.dequeue_stack.size()

	def enqueue(self, value):
		self.enqueue_stack.push(value)

	def dequeue(self):
		if self.size() == 0:
			raise Exception('dequeuing from an empty queue')

		if self.size() == self.enqueue_stack.size():
			self.move_stacks()

		return self.dequeue_stack.pop()

	def move_stacks(self):
		while self.enqueue_stack.size() > 0:
			self.dequeue_stack.push(self.enqueue_stack.pop())
