# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast_pointer = head
        slow_pointer = head
        while slow_pointer and fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer:
                fast_pointer = fast_pointer.next
            else:
                return False
            if slow_pointer == fast_pointer:
                return True
        return False


lst = '[3,2,0,-4]'
head = stringToListNode(lst)

p2 = head.next
p = head
while p.next: p = p.next
p.next = p2

# p = head
# while p.next: p = p.next

s = Solution()
print(s.hasCycle(head))
