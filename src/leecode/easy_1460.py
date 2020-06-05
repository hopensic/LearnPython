from datetime import datetime
from typing import List

'''
tag: ^1460 ^easy ^array
name: ^(Make Two Arrays Equal by Reversing Sub-arrays)
'''


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr


target = [1, 2,3, 3, 4]
arr = [2, 4, 1, 3]

t1 = datetime.now()
s = Solution()
print(s.canBeEqual(target, arr))
t2 = datetime.now()
print(t2 - t1)
