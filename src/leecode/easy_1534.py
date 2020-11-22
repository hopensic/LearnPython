from datetime import datetime
from typing import List

'''
tag: ^1534 ^easy ^array
name: ^(Count Good Triplets)
'''


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        le = len(arr)
        res = 0
        for i in range(le):
            for j in range(i + 1, le):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, le):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    res += 1
        return res


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

t1 = datetime.now()
s = Solution()
print(s.countGoodTriplets(arr, a, b, c))
t2 = datetime.now()
print(t2 - t1)
