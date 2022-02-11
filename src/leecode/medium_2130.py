from datetime import datetime
from leecode.common.common_class import ListNode

'''
tag: ^2130 ^medium ^linkedlist ^two-pointers ^stack
name: ^(Maximum Twin Sum of a Linked List)
'''


class Solution:
    def pairSum(self, head: ListNode) -> int:
        res = -1
        n = 1
        tmp = head
        while tmp.next:
            n = n + 1
            tmp = tmp.next
        tail = tmp
        tmp = head

        if n == 2:
            return head.val + head.next.val
        t = n / 2
        # 取中间偏右一个
        while t > 0:
            tmp = tmp.next
            t -= 1
        cur = tmp
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        while tail:
            if tail.val + head.val > res:
                res = tail.val + head.val
            tail = tail.next
            head = head.next
        return res


a = ListNode(1)
b = ListNode(100000)
a.next = b

t1 = datetime.now()
s = Solution()
print(s.pairSum(a))
t2 = datetime.now()
print(t2 - t1)
