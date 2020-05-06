from collections import Counter
from datetime import datetime
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v > len(nums) / 2:
                return k
        return 0


str1 = [2, 2, 1, 1, 1, 2, 2]
t1 = datetime.now()
s1 = Solution()
print(s1.majorityElement(str1))
t2 = datetime.now()
print(t2 - t1)
