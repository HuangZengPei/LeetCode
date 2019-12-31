# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:return
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # 定位到要翻转的前驱
        for i in range(1,m):
            prev = prev.next
        head = prev.next
        for i in range(m,n):
            nex = head.next
            head.next = nex.next
            nex.next = prev.next
            prev.next = nex
        return dummy.next
        
        
    def reverseBetween(self, head, m, n):
        # 先找到节点，再翻转m到n，再连接节点
        if not head:return
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        for i in range(1,m):
            left = left.next
        head = left.next
        node = head
        prev = None
        for i in range(m,n+1):
            next = node.next
            node.next = prev
            prev = node
            node = next
        head.next = next
        left.next = prev
        return dummy.next
        
        