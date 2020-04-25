from collections import defaultdict
from datetime import datetime
import bisect


class Solution:
    def canJump(self, nums: list) -> bool:
        le = len(nums)
        if le == 0:
            return False
        # 遍历nums 计算每一个i可以到达的最远距离
        max_reach = 0
        for idx, i in enumerate(nums):
            if max_reach >= le - 1:
                return True
            if idx > max_reach:
                return False
            max_reach = max(max_reach, idx + i)
        return False


# arr = [2, 3, 1, 1, 4]
arr = [1]
t1 = datetime.now()
s = Solution()
print(s.canJump(arr))
t2 = datetime.now()
print(t2 - t1)
