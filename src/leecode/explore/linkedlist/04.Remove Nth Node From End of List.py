# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = head
        while n > 1:
            n -= 1
            fast = fast.next
        if not fast.next:
            return head.next
        fast = fast.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


arr = '[1,2,3]'
n = 2
lst = stringToListNode(arr)

# p = head
# while p.next: p = p.next

s = Solution()
print(s.removeNthFromEnd(lst, n))
