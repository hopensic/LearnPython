from datetime import datetime
from typing import List

'''
tag: ^1502 ^easy ^array ^sort
name: ^(Can Make Arithmetic Progression From Sequence)
'''


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != d:
                return False
        return True


arr = [1,2,4]

t1 = datetime.now()
s = Solution()
print(s.canMakeArithmeticProgression(arr))
t2 = datetime.now()
print(t2 - t1)
