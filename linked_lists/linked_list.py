# Now this is a copy of the stack placed under data structure
# but all the excersices in this folder are based on this one
# if the other change we dont want to break interface for the excersices

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next