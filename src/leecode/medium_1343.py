from datetime import datetime
from typing import List

'''
tag: ^1343 ^medium ^array
name: ^(Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold)
'''


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        t = k * threshold
        res = 0
        sums = sum(arr[:k])
        if sums >= t:
            res += 1
        for i in range(k, len(arr)):
            sums += arr[i] - arr[i - k]
            if sums >= t:
                res += 1
        return res


arr1 = [5]
k = 3
threshold = 5

t1 = datetime.now()
s = Solution()
print(s.numOfSubarrays(arr1, k, threshold))
t2 = datetime.now()
print(t2 - t1)
