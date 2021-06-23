import random
import numpy as np
from datetime import datetime
from typing import List

'''
tag: ^1877 ^medium ^greedy ^sort
name: ^(Minimize Maximum Pair Sum in Array)
'''


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        res = [(nums[i] + nums[-(i + 1)]) for i in range(len(nums) // 2)]
        return max(res)


arr1 = np.random.randint(10000, size=10)

t1 = datetime.now()
s = Solution()
print(s.minPairSum(arr1))
t2 = datetime.now()
print(t2 - t1)
