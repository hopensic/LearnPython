from datetime import datetime
from collections import Counter
from typing import List

'''
tag: ^041 ^array ^hash-table
name: ^( First Missing Positive)
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        le = len(nums)
        for idx, i in enumerate(nums):
            if i <= 0 or i > le or i == idx + 1:
                continue
            t = i
            nums[idx] = -1
            while t <= le:
                k = nums[t - 1]
                if k <= 0 or k > le or t == k:
                    nums[t - 1] = t
                    break
                else:
                    nums[t - 1] = t
                    t = k
        for i in range(le):
            if i + 1 == nums[i]:
                continue
            else:
                return i + 1
        else:
            return i + 2


# arr1 = [1, 1]
# arr1 = [3, 4, 2, 6, 1]
arr1 = [3, 4, -1, 1]
# arr1 = [7,8,9,11,12]

t1 = datetime.now()
s = Solution()
print(s.firstMissingPositive(arr1))
t2 = datetime.now()
print(t2 - t1)
