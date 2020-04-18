from collections import Counter
from _collections import defaultdict
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

from datetime import datetime


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_head = head
        n = 1
        while True:
            if head.next is not None:
                n += 1
                head = head.next
            else:
                break
            if head.next is not None:
                n += 1
                head = head.next
                slow_head = slow_head.next
            else:
                break
        if n % 2 == 0:
            return slow_head.next
        else:
            return slow_head


arr1 = '[1]'
lstnode = stringToListNode(arr1)
t1 = datetime.now()
s = Solution()
print(s.middleNode(lstnode).val)
t2 = datetime.now()
print(t2 - t1)
