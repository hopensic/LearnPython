from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(int(len(s) / 2)):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


costs = ["h"]
t1 = datetime.now()
s1 = Solution()
print(s1.reverseString(costs))
t2 = datetime.now()
print(t2 - t1)
