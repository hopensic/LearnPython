from datetime import datetime
from typing import List

'''
tag: ^1829 ^medium ^bit-manipulation
name: ^(Maximum XOR for Each Query)
'''


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        max_value = 2 ** maximumBit - 1
        x = 0
        for i in nums:
            x ^= i
            res.append(max_value ^ x)
        res.reverse()
        return res


nums =  [0,1,2,2,5,7]
maximumBit = 3

t1 = datetime.now()
s = Solution()
print(s.getMaximumXor(nums, maximumBit))
t2 = datetime.now()
print(t2 - t1)
