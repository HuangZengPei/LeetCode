# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # 递归写法
    def preOrder(self,p,list):
            if p == None:
                return 
            else:
                list.append(p.val)
                self.preOrder(p.left,list)
                self.preOrder(p.right,list)
                
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preOrder(root,res)
        return res
        
    # 迭代写法
    def preorderTraversal(self,root):
        if not root:
            return []
        
        stack = [root]  # 保存遍历结点
        res = []  # 保存遍历的结果
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res