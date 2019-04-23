# Taken from: https://www.youtube.com/watch?v=nOcFiGl5Vy4&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=19
from tree import BinaryTree

def is_balanced_helper(tree):
	if not tree:
		return True, 0

	balanced_left, depth_left = is_balanced_helper(tree.left_child)
	balanced_right, depth_right = is_balanced_helper(tree.right_child)
	
	diff = abs(depth_right - depth_left)
	if not balanced_left or not balanced_right or diff > 1:
		return False, max(depth_left, depth_right) + 1
	return True, max(depth_left, depth_right) + 1

def is_balanced(tree):
	return is_balanced_helper(tree)[0]

n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n8 = BinaryTree(8)
n9 = BinaryTree(9)
n10 = BinaryTree(10)
n11 = BinaryTree(11)
n12 = BinaryTree(12)
n13 = BinaryTree(13)

n1.left_child = n2
n1.right_child = n3

n2.left_child = n4
n2.right_child = n5

n3.left_child = n6
n3.right_child = n7

n4.right_child = n8

n6.left_child = n9
n6.right_child = n10

n7.left_child = n11
n7.right_child = n12

n9.left_child = n13

print('is_balanced for a balanced tree is: ', is_balanced(n1))

n14 = BinaryTree(14)
n13.left_child = n14

print('is_balanced for a non balanced tree is: ', is_balanced(n1))