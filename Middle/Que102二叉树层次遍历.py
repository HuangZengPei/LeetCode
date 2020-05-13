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
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res = []
        nodes = []
        nodes.append(root)
        while nodes:
            single_level = []
            single_nodes = []
            # 单层遍历
            for node in nodes:
                single_level.append(node.val)
                if node.left:
                    single_nodes.append(node.left)
                if node.right:
                    single_nodes.append(node.right)
            res.append(single_level)
            nodes = single_nodes
        return res