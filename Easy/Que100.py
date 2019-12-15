# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # 不能单独用前序遍历，[1,2]以及[1,null,2]结果相同
    def preOrder(self,p,list):
            if p == None:
                return 
            else:
                list.append(p.val)
                self.preOrder(p.left,list)
                self.preOrder(p.right,list)
                
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """        
        list1 = []
        list2 = []
        self.preOrder(p,list1)
        self.preOrder(q,list2)
        return list1 == list2
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)