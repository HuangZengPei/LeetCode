class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        在每次生成一个节点后再多生成一个节点，用来判断最后一位还有没有
        """
        n = l1.val + l2.val
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1, p2,p3 = l1.next, l2.next, l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum//10)
                p1, p2, p3 = p1.next,p2.next,p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1, p3 = p1.next, p3.next
            elif p2 and not p1:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2, p3 = p2.next, p3.next
            else:
                if p3.next.val ==0:
                    p3.next = None
                break
        return l3