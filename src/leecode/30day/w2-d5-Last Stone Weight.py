from leecode.common.official import stringToTreeNode
from leecode.common.common_class import TreeNode
from datetime import datetime

from bisect import insort


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x != y:
                insort(stones, y - x)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0


arr = [1,1]
t1 = datetime.now()
s = Solution()
print(s.lastStoneWeight(arr))
t2 = datetime.now()
print(t2 - t1)
