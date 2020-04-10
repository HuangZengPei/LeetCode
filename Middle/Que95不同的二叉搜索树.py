# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTrees_(start,end):
            if start > end:
                return [None,]
            
            results = []
            for i in range(start,end+1):
                left = generateTrees_(start,i-1)
                right = generateTrees_(i+1,end)
                
                for l in left:
                    for r in right:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        results.append(currTree)
                        
            return results
        
        return generateTrees_(1,n) if n else []
        

        