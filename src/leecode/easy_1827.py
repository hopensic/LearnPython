from datetime import datetime
from typing import List

'''
tag: ^1827 ^easy ^array ^greedy
name: ^(Minimum Operations to Make the Array Increasing)
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return res
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return res


arr1 = [1, 5, 2, 4, 1]

t1 = datetime.now()
s = Solution()
print(s.minOperations(arr1))
t2 = datetime.now()
print(t2 - t1)
