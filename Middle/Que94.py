# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self,p,list):
        if not p:
            return list
        if p.left:
            self.inOrder(p.left,list)
        list.append(p.val)
        self.inOrder(p.right,list)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inOrder(root,res)
        return res
        
        
    # 迭代版本
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        if root.left:
            stack = [root.left]
            node = root.left
        else:
            stack = [root]
            node = root
        res = []
        while stack:
            while node:
                stack.append(node)
                node = node.left
            # 走到最左孩子，这时弹出，右孩子为空
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
            
        