class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeList = set()
        while head is not None:
            if head in nodeList:
                return head
            else:
                nodeList.add(head)
                head = head.next
        return None
        
    
    # 快慢指针,第一阶段，寻找到相遇点，判断是否有环
     def getIntersect(self, head):
        fast = slow = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return slow
        return None
        
    # 第二阶段，一个指针指向头，一个指向相遇点。每次移动一步，相遇时即为环的入口。
    def detectCycle(self, head):
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1,ptr2 = ptr1.next,ptr2.next
        return ptr1