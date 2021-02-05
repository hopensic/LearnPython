from datetime import datetime
from typing import List
import re

'''
tag: ^1689 ^medium ^greedy
name: ^(Partitioning Into Minimum Number Of Deci-Binary Numbers)
'''


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))


arr1 = "82734"
# arr1 = "31131003"
# arr1 = "32"

t1 = datetime.now()
s = Solution()
print(s.minPartitions(arr1))
t2 = datetime.now()
print(t2 - t1)
