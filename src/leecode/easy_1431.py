from datetime import datetime
from typing import List

'''
tag: ^1431 ^easy ^array
name: ^(Kids With the Greatest Number of Candies)
'''


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [candy + extraCandies >= max_value for candy in candies]



candies = [2, 3, 5, 1, 3]
extraCandies = 3

t1 = datetime.now()
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))
t2 = datetime.now()
print(t2 - t1)
