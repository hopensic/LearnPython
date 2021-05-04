from datetime import datetime
from typing import List

'''
tag: ^1822 ^easy ^math
name: ^(Sign of the Product of an Array)
'''


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num_of_minus = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                num_of_minus += 1
        return 1 if num_of_minus % 2 == 0 else -1


nums =  [-1,1,-1,1,-1]

t1 = datetime.now()
s = Solution()
print(s.arraySign(nums))
t2 = datetime.now()
print(t2 - t1)
