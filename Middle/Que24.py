# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return None
        thread = ListNode(0)
        thread.next = head
        c = thread
        while c.next and c.next.next:
            a,b = c.next,c.next.next
            c.next = b
            c.next.next = b.next
            b.next = a
            c= c.next.next
        return thread.next
