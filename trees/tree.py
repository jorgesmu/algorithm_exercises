# Now this is are copies of the trees placed under data structure
# but all the excersices in this folder are based on this ones
# if the other change we dont want to break interface for the excersices

class Tree:
	def __init__(self, value, id=''):
		self.children = []
		self.value = value
		self.id = id


class BinaryTree:
	def __init__(self, value, left_child=None, right_child=None, id=''):
		self.left_child = left_child
		self.right_child = right_child
		self.value = value	
