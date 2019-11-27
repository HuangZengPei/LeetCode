# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(list1,list2):
            if not list1 and not list2:
                return None
            if list1 and not list2:
                return list1
            if not list1 and list2:
                return list2
            if list1.val < list2.val:
                p = list1
                list1 = list1.next
            else:
                p = list2
                list2 = list2.next
            head = p
            while list1 and list2:
                if list1.val < list2.val:
                    p.next = list1
                    p = p.next
                    list1 = list1.next
                else:
                    p.next = list2
                    p = p.next
                    list2 = list2.next
            while list1:
                p.next = list1
                p = p.next
                list1 = list1.next
            while list2:
                p.next = list2
                p = p.next
                list2 = list2.next
            return head


        # 对k个链表两两合并
        if not lists: return None
        res = lists[0]
        for i in range(1,len(lists)):
            res = merge(res,lists[i])
        return res



"""
官方解法，使用优先级队列
"""
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


test = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(1)
list2.next = ListNode(4)
head = test.merge(list1,list2)
while head:
    print(head.val)
    head = head.next
