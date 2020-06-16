from datetime import datetime
from typing import List

'''
tag: ^1480 ^easy ^array
name: ^(Running Sum of 1d Array)
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


arr1 = [3, 1, 2, 10, 1]

t1 = datetime.now()
s = Solution()
print(s.runningSum(arr1))
t2 = datetime.now()
print(t2 - t1)
