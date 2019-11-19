# Definition for singly-linked list.
# Description: 合并两个有序链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 判断输入，两个为空或者一个为空
        if not l1 and not l2:return None
        if not l1 and l2:return l2
        if l1 and not l2:return l1
        p1 = l1
        p2 = l2
        # 初始化第一个节点之后，要将另外一个节点赋值给开始节点，不能直接操作初始节点，否则返回不是从初始节点开始
        result = ListNode(min(p1.val,p2.val))
        if p1.val <= p2.val:
            p1 = p1.next
        else: p2 = p2.next
        p = result
        # 两个链表都还有值
        while p1 and p2:
            p.next = ListNode(min(p1.val,p2.val))
            p = p.next
            if p1.val <= p2.val:
                p1 = p1.next
            else: p2 = p2.next
        # 一个链表有值
        while True:
            if not p1 and p2:
                p.next = ListNode(p2.val)
                p = p.next
                p2 = p2.next
                if p2 == None:
                    break
            elif p1 and not p2:
                p.next = ListNode(p1.val)
                p = p.next
                p1 = p1.next
                if p1 == None:
                    break
        return result

test = Solution()
p1 = ListNode(1)
p1.next = ListNode(2)
p1.next.next = ListNode(3)
p2 = ListNode(1)
p2.next = ListNode(4)
p = test.mergeTwoLists(p1,p2)
while p!= None:
    print(p.val)
    p = p.next
