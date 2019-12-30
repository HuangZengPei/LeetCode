# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head = test.reverseList(head)
while head:
    print(head.val)
    head = head.next
            
            
            