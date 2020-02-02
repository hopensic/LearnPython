from datetime import datetime
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

'''
tag: ^160 ^easy ^linkedlist
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        l1 = headA
        l2 = headB
        while l1 is not l2:
            if l1.next or l2.next:
                l1 = headB if l1.next is None else l1.next
                l2 = headA if l2.next is None else l2.next
            else:
                return None
        else:
            return l1


# h1 = stringToListNode('[4,1]')
# h2 = stringToListNode('[5,0,1]')
# h3 = stringToListNode('[8,4,5]')
h1 = stringToListNode('[2,6,4]')
h2 = stringToListNode('[1,5]')
h3 = stringToListNode('[]')
top1 = h1
top2 = h2
while h1.next:
    h1 = h1.next
while h2.next:
    h2 = h2.next
if h3 is not None:
    h1.next = h3
    h2.next = h3

t1 = datetime.now()
s = Solution()
print(s.getIntersectionNode2(top1, top2))
t2 = datetime.now()
print(t2 - t1)
