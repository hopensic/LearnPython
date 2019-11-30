# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from leecode.common.common_class import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre = ListNode('x')
        pre.next = head
        i = 0
        while head is not None:
            i += 1
            if i % 2 == 0:
                pre = pre.next
            head = head.next
        return pre.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
# n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# n5.next = n6

s = Solution()
r = s.middleNode(n1)
print('------')
