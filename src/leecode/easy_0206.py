from datetime import datetime
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

'''
tag: ^206 ^easy ^linkedlist
name: ^(Reverse Linked List)
'''


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        stacks = []
        while head:
            stacks.append(head)
            head = head.next
        if stacks:
            top = stacks.pop()
        cur = top
        while stacks:
            cur.next = stacks.pop()
            cur = cur.next
        cur.next = None
        return top


h1 = stringToListNode('[2,6,4]')

t1 = datetime.now()
s = Solution()
print(s.reverseList(h1))
t2 = datetime.now()
print(t2 - t1)
