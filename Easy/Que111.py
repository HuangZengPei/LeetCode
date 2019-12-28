# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.minDepth(root.left) 
            right_height = self.minDepth(root.right) 
            if not root.left or not root.right:# 只有左子树或者只有右子树
                return max(left_height, right_height) + 1
            return min(left_height, right_height) + 1