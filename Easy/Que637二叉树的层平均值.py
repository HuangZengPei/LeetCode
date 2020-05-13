class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
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
            res.append(sum(single_level)/len(single_level))
            nodes = single_nodes
        return res
        