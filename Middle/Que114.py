# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 将二叉树展开为链表，使用栈保存右子树
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:return 
        stack = []
        stack.append(root)
        pre = None
        while stack:
            temp = stack.pop()
            if pre:
                pre.right = temp
                pre.left = None
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            pre = temp