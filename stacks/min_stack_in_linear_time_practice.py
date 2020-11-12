# Taken from: https://www.youtube.com/watch?v=ufwPuyxkNVE
from stack import Stack

# We can also implemented with another supporting stack as in the video
# we will be saving some memory but the space complexity will be the same
class MinStack:
	def __init__(self):
		self.stack = Stack()
		self.min_stack = Stack()
	def push(self, element):
		self.stack.push(element)
		if self.min_stack.size() == 0 or element <= self.min_stack.seek():
			self.min_stack.push(element)
		return
	def pop(self):
		element = self.stack.pop()
		if element == self.min_stack.seek():
			self.min_stack.pop()
		return element

	def min(self):
		return self.min_stack.seek()

	def size(self):
		return self.stack.size()

def push(stack, element):
	print('Pushing: ', element)
	stack.push(element)
	print('minimum: ', stack.min())

def pop(stack):
	element = stack.pop()
	print('Popped: ', element)
	print('minimum: ', stack.min())

stack = MinStack()
print('stack created, min: ', stack.min())
push(stack, 11)
push(stack, 10)
push(stack, 12)
push(stack, 9)
push(stack, 15)
while stack.size() > 0:
	pop(stack)
