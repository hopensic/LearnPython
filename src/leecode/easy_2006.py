from datetime import datetime
from typing import List

'''
tag: ^2006 ^easy ^array
name: ^(Count Number of Pairs With Absolute Difference K)
'''


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = res + 1 if abs(nums[i] - nums[j]) == k else res

        return res


nums = [3,2,1,5,4]
k = 2

t1 = datetime.now()
s = Solution()
print(s.countKDifference(nums, k))
t2 = datetime.now()
print(t2 - t1)
