from collections import Counter
from datetime import datetime
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        h = node
        while h:
            n = h.next
            h.val = n.val
            if not n.next:
                h.next = None
                break
            h = h.next


head = '[4,5,1,9]'
h = stringToListNode(head)
node = 5
t1 = datetime.now()
s1 = Solution()
print(s1.deleteNode(h))
t2 = datetime.now()
print(t2 - t1)
