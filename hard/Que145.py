# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    
    # 递归版本
    def postorder(self,root,list):
        if not root:
            return list
        self.postorder(root.left,list)
        self.postorder(root.right,list)
        list.append(root.val)
            
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorder(root,res)
        return res
        
    # 迭代版本
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        # 这里使用一个双端队列，直接在首部O(1)的插入元素，避免逆序整个栈
        res = deque()
        if root is None:
            return None
      
        stack.append(root)
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            # 先压左 在压右
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res