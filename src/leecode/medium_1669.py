from datetime import datetime
from typing import List

'''
tag: ^1669 ^medium ^linkedlist
name: ^(Merge In Between Linked Lists)
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = list1
        loop_list2 = list2
        dif = b - a + 1
        while a > 1:
            list1 = list1.next
            a -= 1
        loop_list1 = list1
        while dif > 0:
            loop_list1 = loop_list1.next
            dif -= 1
        list1_tail = loop_list1.next
        while loop_list2.next:
            loop_list2 = loop_list2.next
        loop_list2.next = list1_tail
        list1.next = list2
        return res


arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]

a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

b0 = ListNode(1000000)
b1 = ListNode(1000001)
b2 = ListNode(1000002)
b0.next = b1
b1.next = b2

t1 = datetime.now()
s = Solution()
print(s.mergeInBetween(a0, 3, 4, b0))
t2 = datetime.now()
print(t2 - t1)
