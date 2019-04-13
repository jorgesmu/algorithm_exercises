# Now this is a copy of the stack placed under data structure
# but all the excersices in this folder are based on this one
# if the other change we dont want to break interface for the excersices
class Stack:
	def __init__(self):
		self.array = []

	def push(self, element):
		self.array.append(element)

	def pop(self):
		if self.size() == 0:
			return None
		return self.array.pop()

	def size(self):
		return len(self.array)

	def seek(self):
		if self.size() == 0:
			return None
		return self.array[-1]