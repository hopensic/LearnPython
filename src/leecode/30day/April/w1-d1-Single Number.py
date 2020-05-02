from collections import Counter
from datetime import datetime


class Solution:
    def singleNumber(self, nums: list) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k
        return None


arr1 = [4, 1, 2, 1, 2]

t1 = datetime.now()
s = Solution()
print(s.singleNumber(arr1))
t2 = datetime.now()
print(t2 - t1)
