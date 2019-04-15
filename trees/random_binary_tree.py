import random
class BinaryTree:

	def __init__(self, value):
		self.__size = 1
		self.__value = value
		self.__left_child = self.__right_child = None

	def set_left_child(self, tree):
		# TODO: update size when childs are added to the children (notify the parent)
		self.__left_child = tree
		self.__size += tree.size()

	def set_right_child(self, tree):
		self.__right_child = tree
		self.__size += tree.size()

	def size(self):
		return self.__size

	def value(self):
		return self.__value

	def left_child(self):
		return self.__left_child

	def right_child(self):
		return self.__right_child
		
	def random(self, hops):
		number_of_hops = random.randrange(self.__size)
		return self.__recursively_search(self, number_of_hops)

	def __recursively_search(self, tree, missing_hopes):
		if missing_hopes == 0:
			return tree.value()
		missing_hopes -=1
		if tree.left_child().size() - 1 >= missing_hopes:
			return self.__recursively_search(tree.left_child(), missing_hopes)
		return self.__recursively_search(tree.right_child(), missing_hopes - tree.left_child().size())

root = BinaryTree(4)

t2 = BinaryTree(2)
t3 = BinaryTree(6)
t4 = BinaryTree(1)
t5 = BinaryTree(3)
t6 = BinaryTree(5)
t7 = BinaryTree(7)

t3.set_left_child(t6)
t3.set_right_child(t7)
t2.set_left_child(t4)
t2.set_right_child(t5)
root.set_left_child(t2)
root.set_right_child(t3)

for i in range(15):
	print(root.random(i))
	