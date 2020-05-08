# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        while head:
            if head.val != val:
                break
            head = head.next
        else:
            return None
        o_head = head
        pre = head
        head = head.next
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return o_head


arr = '[1,2,3,4,6,7]'
lst = stringToListNode(arr)


s = Solution()
print(s.removeElements(lst, 6))
