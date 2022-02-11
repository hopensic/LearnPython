from datetime import datetime
from typing import List

'''
tag: ^1929 ^easy ^array
name: ^(Concatenation of Array)
'''


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


arr1 =  [1,3,2,1]

t1 = datetime.now()
s = Solution()
print(s.getConcatenation(arr1))
t2 = datetime.now()
print(t2 - t1)
