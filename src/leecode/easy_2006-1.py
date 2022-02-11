from collections import Counter
from datetime import datetime
from typing import List

'''
tag: ^2006 ^easy ^array
name: ^(Count Number of Pairs With Absolute Difference K)
'''


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        c = Counter(nums)
        lst = list(c.keys())
        lst.sort(reverse=True)

        for i in range(len(lst)):
            j = i + 1
            while j < len(lst):
                if lst[i] - lst[j] > k:
                    break
                elif lst[i] - lst[j] == k:
                    res += c[lst[i]] * c[lst[j]]
                    break
                j = j + 1
        return res


nums = [1]
k = 2

t1 = datetime.now()
s = Solution()
print(s.countKDifference(nums, k))
t2 = datetime.now()
print(t2 - t1)
