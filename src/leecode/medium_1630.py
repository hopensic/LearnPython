from datetime import datetime
from typing import List

'''
tag: ^1630 ^medium ^sort
name: ^(Arithmetic Subarrays)
'''


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []






# nums = [4, 6, 5, 9, 3, 7]
# l = [0, 0, 2]
# r = [2, 3, 5]

nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
left = [0, 1, 6, 4, 8, 7]
right = [4, 4, 9, 7, 9, 10]
nums.sort()


t1 = datetime.now()
s = Solution()
print(s.checkArithmeticSubarrays(nums, left, right))
t2 = datetime.now()
print(t2 - t1)
