# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = head
        while head.next:
            to_transfer = head.next
            head.next = to_transfer.next
            to_transfer.next = new_head
            new_head = to_transfer
        return new_head


arr = '[1]'
lst = stringToListNode(arr)



s = Solution()
print(s.reverseList(lst))
