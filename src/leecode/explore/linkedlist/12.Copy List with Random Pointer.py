from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pre = dummy1 = head
        while head:
            node = Node(head.val)
            node.next = head.next
            head.next = node
            head = head.next.next
        while pre:
            new_head = pre.next
            new_head.random = pre.random.next if pre.random else None
            pre = new_head.next
            new_head.next = pre.next if pre else None
        return dummy1.next


a1 = Node(7)
a2 = Node(13)
a3 = Node(11)
a4 = Node(10)
a5 = Node(1)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = None

a1.random = None
a2.random = a1
a3.random = a5
a4.random = a3
a5.random = a1

s = Solution()
print(s.copyRandomList(a1))
