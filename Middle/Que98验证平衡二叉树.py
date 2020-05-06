# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def DFS(root,left, right):
            if root is None:
                return True
                
            if left < root.val < right:
                return DFS(root.left,left, root.val) and DFS(root.right, root.val, right)
            else:
                return False
        return DFS(root, -float('inf'), float('inf'))