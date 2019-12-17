# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    # 二叉树的层次遍历，但是从最底层遍历，
    def singleLevelOrder(self,nodelist):
        if not nodelist:
            return None
        singelLevel = []
        for node in nodelist:
            singelLevel.append(node.val)
        return singelLevel
        
    def levelOrderBottom(self, root):
        if not root:return []
        res = deque()
        level = [root]
        nextLevel = []
        while level:
            res.appendleft(self.singleLevelOrder(level))
            for node in level:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            level = nextLevel.copy()
            nextLevel = []
        return res