from datetime import datetime
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

'''
tag: ^1290 ^easy
name: ^(Convert Binary Number in a Linked List to Integer)
'''


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        while True:
            lst.append(str(head.val))
            if head.next:
                head = head.next
            else:
                break
        return int(''.join(lst), 2)


arr1 = '[0,0]'
listnode = stringToListNode(arr1)

t1 = datetime.now()
s = Solution()
print(s.getDecimalValue(listnode))
t2 = datetime.now()
print(t2 - t1)
