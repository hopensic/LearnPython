from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1512 ^easy ^array ^hash-table ^math
name: ^(Number of Good Pairs)
'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for i in nums:
            res += dic[i]
            dic[i] += 1
        return res


arr1 = [1, 2,3]

t1 = datetime.now()
s = Solution()
print(s.numIdenticalPairs(arr1))
t2 = datetime.now()
print(t2 - t1)
