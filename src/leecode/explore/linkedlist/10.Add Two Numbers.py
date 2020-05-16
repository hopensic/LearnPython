# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n, mod, digit = 0, 0, 1
        dummy = d = ListNode(0)

        while l1 and l2:
            n = l1.val + l2.val + mod
            if n > 9:
                mod = 1
                n -= 10
            else:
                mod = 0
            d.next = ListNode(n)
            d = d.next
            l1 = l1.next
            l2 = l2.next

        def getRemain(node: ListNode):
            nonlocal mod, d
            while node:
                n = node.val + mod
                if n > 9:
                    mod = 1
                    n -= 10
                else:
                    mod = 0
                d.next = ListNode(n)
                d = d.next
                node = node.next

        getRemain(l1)
        getRemain(l2)

        if mod == 1:
            d.next = ListNode(1)
        return dummy.next


arr1 = '[5]'
lst1 = stringToListNode(arr1)

arr2 = '[5]'
lst2 = stringToListNode(arr2)

s = Solution()
print(s.addTwoNumbers(lst1, lst2))
