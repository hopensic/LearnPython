"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Node:
    def __init__(self, val):
        # self.val = val
        # self.prev = prev
        # self.next = next
        # self.child = child
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        def get_sub(parent: Node, child: Node):
            next_node = parent.next
            parent.next = child
            child.prev = parent
            parent.child = None


            while child.next:
                if child.child:
                    get_sub(child, child.child)
                child = child.next
            if child.child:
                get_sub(child,child.child)
            if next_node:
                next_node.prev = child
                child.next=next_node

        dummy = Node(-1)
        dummy.child = head
        get_sub(dummy, head)
        head.prev=None
        return head


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 = Node(8)
a9 = Node(9)
a10 = Node(10)
a11 = Node(11)
a12 = Node(12)

# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
# a5.next = a6
#
# a6.prev = a5
# a5.prev = a4
# a4.prev = a3
# a3.prev = a2
# a2.prev = a1
#
# a3.child=a7
#
# a7.next = a8
# a8.next = a9
# a9.next = a10
#
# a10.prev = a9
# a9.prev = a8
# a8.prev = a7
#
# a8.child=a11
#
# a11.next=a12
# a12.prev=a11
a1.child=a2
a2.child=a3



s = Solution()
print(s.flatten(a1))
