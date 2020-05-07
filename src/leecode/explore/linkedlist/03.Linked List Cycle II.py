# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast_pointer = head
        slow_pointer = head
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer:
                fast_pointer = fast_pointer.next
            else:
                return None
            # 找到cycle内的一个点
            if slow_pointer == fast_pointer:

                # 遍边一遍cycle看是否等于head
                def is_include_head(root: ListNode):
                    p = root.next
                    while p != root:
                        if p == head:
                            return p
                        else:
                            p = p.next
                    if p == head:
                        return True, p
                    else:
                        return False, None

                while True:
                    # 需要遍边一遍cycle看是否等于head
                    is_include, node = is_include_head(slow_pointer)
                    if is_include:
                        return node
                    slow_pointer = slow_pointer.next
                    head = head.next

        return None


lst = '[3,2,0,-4]'
head = stringToListNode(lst)

p2 = head.next
p = head
while p.next: p = p.next
p.next = p2

# p = head
# while p.next: p = p.next

s = Solution()
print(s.detectCycle(head))
