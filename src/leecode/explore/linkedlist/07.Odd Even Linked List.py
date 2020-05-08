# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd_head = head
        loop_odd_pointer = odd_head
        head =head.next
        even_head = head
        loop_even_pointer = even_head
        if not even_head:
            return odd_head
        while head and head.next:
            head = head.next
            loop_odd_pointer.next=head
            loop_odd_pointer=loop_odd_pointer.next
            head =head.next
            if head:
                loop_even_pointer.next=head
                loop_even_pointer=loop_even_pointer.next
            else:
                loop_even_pointer.next=None
                loop_odd_pointer.next=even_head
        else:
            loop_even_pointer.next = None
            loop_odd_pointer.next = even_head
        return odd_head









arr = '[1,2,3,4,5,6,7]'
lst = stringToListNode(arr)

s = Solution()
print(s.oddEvenList(lst))
