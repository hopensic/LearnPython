from datetime import datetime
from typing import List

'''
tag: ^1920 ^easy ^array ^simulation
name: ^(Build Array from Permutation)
'''


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


nums = [5,0,1,2,3,4]

t1 = datetime.now()
s = Solution()
print(s.buildArray(nums))
t2 = datetime.now()
print(t2 - t1)
