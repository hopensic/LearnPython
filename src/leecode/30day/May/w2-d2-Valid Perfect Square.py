from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            k = i * i
            if k > num:
                return False
            if k == num:
                return True


num = 16
t1 = datetime.now()
s1 = Solution()
print(s1.isPerfectSquare(num))
t2 = datetime.now()
print(t2 - t1)
