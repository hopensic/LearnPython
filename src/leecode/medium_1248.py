import operator
from collections import defaultdict
from datetime import datetime
from itertools import accumulate

'''
tag: ^1248 ^medium ^two-pointers
name: ^(Count Number of Nice Subarrays)
'''


class Solution:
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        res = 0
        dic = defaultdict(int)
        for idx, num in enumerate(accumulate(map(lambda x: x % 2, nums), operator.add)):
            dic[num] += 1
            res = res + 1 if num == k else res
            res += dic[num - k]
        return res


arr1 = [1,1,2,1,1]
k1 = 3

t1 = datetime.now()
s = Solution()
print(s.numberOfSubarrays(arr1, k1))
t2 = datetime.now()
print(t2 - t1)
