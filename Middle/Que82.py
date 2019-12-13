# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :description:删除链表中出现的重复项
        """
        if head == None or head.next == None:
            return head
        fakeHead = ListNode(-1)
        pre = fakeHead
        fakeHead.next = head
        while head!= None and head.next!= None:
            if head.val != head.next.val:
                pre = head
                head = head.next
            else:
                while head.val == head.next.val:
                    head = head.next
                if head == null:
                    pre.next = null
                else:
                    pre.next = head.next
                    head = head.next
        return fakeHead.next
        # 递归版本，存在问题
        # repeat = False
        # if head == None or head.next == None:
        #     return head
        # while head!= None and head.next != None:
        #     if head.val == head.next.val:
        #         head = head.next
        #         repeat = True
        #     else:
        #         if repeat:
        #             head = head.next
        #             self.deleteDuplicates(head)
        #         else:
        #             self.deleteDuplicates(head.next)
        # return head