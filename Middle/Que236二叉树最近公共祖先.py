# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:return None
        stackp = []
        stackq = []
        self.findPath(root,p,stackp)
        self.findPath(root,q,stackq)
        res,i = stackp[0],0
        while i < len(stackp) and i < len(stackq) and stackp[i] == stackq[i]:
            res = stackp[i]
            i += 1
        return res
        
        
    # 这种写法最后会弹出栈
    def findPath(self,root,target,ans):
        if root is None:
            return False
        ans.append(root)
        if root.val == target.val:
            return True
        elif self.findPath(root.left,target,ans) or self.findPath(root.right,target,ans):
             return True
        ans.pop()
        
root = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)
root.left = node5
root.right = node1
node5.left = node6
node5.right = node2
node2.left = node7
node2.right = node4
node1.left = node0
node1.righ1 = node8

ans = []
Solution().findPath(root,node6,ans)
def printAns(anses):
    for ans in anses:
        print(ans.val)
printAns(ans)