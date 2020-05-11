# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif (not s and t) or (s and not t):
            return False
        else:
            return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
    def isSameTree(self,s,t):
        if not s and not t:
            return True
        elif (not s and t) or (s and not t):
            return False
        if s.val == t.val:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right, t.right)
        else:
            return False