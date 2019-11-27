# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        if not head or n <= 0:return None
        if head.next == None and n == 1:return None
        first = head     # 考虑删除头节点的情况
        while first.next != None:
            count += 1
            first = first.next
            if count == n:
                follow = head
            if count > n:
                follow = follow.next
        if count == n-1:   # 删除头节点
            head = head.next
        else:
            p = follow.next.next
            follow.next = p
        return head

test = Solution()
a= ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a = test.removeNthFromEnd(a,4)
while a != None:
    print(a.val)
    a = a.next
