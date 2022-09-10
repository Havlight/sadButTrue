class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ovec = ListNode(-1)
        d = 0
        p = ovec
        p1 = l1
        p2 = l2
        while True:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            tot = v1 + v2 + d
            v = tot % 10
            d = tot // 10
            p.next = ListNode(v)
            p = p.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            if p1 is None and p2 is None:
                if d:
                    p.next = ListNode(d)
                return ovec.next
