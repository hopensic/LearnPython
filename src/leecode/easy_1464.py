from datetime import datetime
from typing import List

'''
tag: ^1464 ^easy ^array
name: ^(Maximum Product of Two Elements in an Array)
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]-1)*(nums[1]-1)


arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]

t1 = datetime.now()
s = Solution()
print(s.maxProduct(arr1))
t2 = datetime.now()
print(t2 - t1)
