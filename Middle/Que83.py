# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        curr = head
        while temp.next != None:
            if temp.val == curr.val:
                temp = temp.next
            else:
                curr.next = temp
                curr = temp
                temp = temp.next
        return head
