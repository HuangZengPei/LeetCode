# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def singleLevelOrder(self,nodelist):
        if not nodelist:
            return None
        singelLevel = []
        for node in nodelist:
            singelLevel.append(node.val)
        return singelLevel

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        level = [root]
        nextLevel = []
        while level:
            res.append(self.singleLevelOrder(level))
            for node in level:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            level = nextLevel.copy()
            nextLevel = []
        return res