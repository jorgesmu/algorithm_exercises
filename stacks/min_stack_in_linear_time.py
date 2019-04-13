# Taken from: https://www.youtube.com/watch?v=ufwPuyxkNVE
from stack import Stack

# We can also implemented with another supporting stack as in the video
# we will be saving some memory but the space complexity will be the same
class MinStack:
	def __init__(self):
		self.stack = Stack()

	def push(self, element):
		if self.stack.size() == 0:
			minimum = element
		else:
			minimum = min(element, self.stack.seek()[1])
		self.stack.push((element, minimum))

	def pop(self):
		element, _ = self.stack.pop()
		return element

	def min(self):
		if self.stack.size() == 0:
			return None
		_, minimum = self.stack.seek()
		return minimum

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
