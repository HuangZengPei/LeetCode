# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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