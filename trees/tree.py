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
