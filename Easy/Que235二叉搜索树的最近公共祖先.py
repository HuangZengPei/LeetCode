# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def findPath(root,target,ans):
            if root is None:
                return ans
            ans.append(root)
            if root.val == target.val:
                return ans
            elif root.val < target.val:
                findPath(root.right,target,ans)
            else:
                findPath(root.left,target,ans)
            if ans[-1] == target:
                return
            ans.pop()
            
        if not root or not p or not q:return None
        stackp = []
        stackq = []
        findPath(root,p,stackp)
        findPath(root,q,stackq)
        
        res,i = stackp[i],0
        while i < len(stackp) and i < len(stackq) and stackp[i] == stackq[i]:
            res = stackp[i]
            i += 1
        return res
        
        
        

        
        

    
root = TreeNode(6)
node5 = TreeNode(5)
node3 = TreeNode(3)
node9 = TreeNode(9)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)
root.left = node2
root.right = node8
node2.left = node0
node2.right = node4
node4.left = node3
node4.right = node5
node8.left = node7
node8.righ1 = node9

def printAns(anses):
    for ans in anses:
        print(ans.val)
        
ans = []
findPath(root,node0,ans)

printAns(ans)