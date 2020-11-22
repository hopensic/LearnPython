from datetime import datetime
from typing import List

'''
tag: ^1588 ^easy ^array
name: ^(Sum of All Odd Length Subarrays)
'''


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        le = len(arr)
        sums = [arr[0]]
        for idx, i in enumerate(arr[1:]):
            sums.append(sums[idx] + i)
        print(sums)
        res = sums[-1]
        d = 3
        while d <= le:
            res += sums[d - 1]
            for i in range(d, le):
                res += sums[i] - sums[i - d]
            d += 2
        return res


# arr1 = [1, 4, 2, 5, 3]
arr1 = [10, 11, 12]

t1 = datetime.now()
s = Solution()
print(s.sumOddLengthSubarrays(arr1))
t2 = datetime.now()
print(t2 - t1)
