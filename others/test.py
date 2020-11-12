# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, id):
        self.val = x
        self.id = id
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node, max_found):
            if not node:
                return 0
            lg = max_gain(node.left, max_found)
            rg = max_gain(node.right, max_found)
            max_found[0] = max(max_found[0], node.val, node.val + lg + rg, node.val + lg, node.val + rg)
            return node.val + max(lg, rg, 0)

        max_found = [float('-inf')]
        max_gain(root, max_found)
        return max_found[0]
t1 = TreeNode(9,1)
t2 = TreeNode(6,2)
t3 = TreeNode(-3,3)
t4 = TreeNode(-6,4)
t5 = TreeNode(2,5)
t6 = TreeNode(2,6)
t7 = TreeNode(-6,7)
t8 = TreeNode(-6,8)
t9 = TreeNode(-6,9)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
t5.left = t6
t6.left = t8
t6.right = t7
t7.left = t9
print(Solution().maxPathSum(t1))