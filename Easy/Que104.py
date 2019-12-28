# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        depth = 1
        stack = []
        stack.append((1,root))
        while stack:
            current_depth,node = stack.pop()
            if node:
                depth = max(depth,current_depth)
                stack.append((current_depth+1, node.left))
                stack.append((current_depth+1, node.right))
        return depth
        
        
    # 递归版本
     def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
