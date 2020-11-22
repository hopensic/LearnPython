from datetime import datetime
from typing import List

'''
tag: ^1470 ^easy ^array
name: ^(Shuffle the Array)
'''


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend(nums[i::n])
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3

t1 = datetime.now()
s = Solution()
print(s.shuffle(nums, n))
t2 = datetime.now()
print(t2 - t1)
