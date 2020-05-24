from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1442 ^medium ^array ^math ^bit-manipulation
name: ^(Count Triplets That Can Form Two Arrays of Equal XOR)
'''


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        if len(arr) == 0:
            return res
        dic = defaultdict(list)
        bitxor_sum = arr[0]
        dic[arr[0]].append(0)
        for i in range(1, len(arr)):
            bitxor_sum ^= arr[i]
            dic[bitxor_sum].append(i)
        for k, lst in dic.items():
            if k == 0:
                res += lst[0]
                for i in range(1, len(lst)):
                    res += lst[i]
                    for j in range(0, i):
                        t = lst[i] - lst[j]
                        res += t-1 if t > 1 else 0
            else:
                for i in range(1, len(lst)):
                    for j in range(0, i):
                        t = lst[i] - lst[j]
                        res += t-1 if t > 1 else 0

        return res


arr1 = [1]
# arr1 = [2, 3, 1, 6, 7]
# arr1 = [1, 1, 1, 1, 1]
# arr1 = [1, 1, 1, 1]

t1 = datetime.now()
s = Solution()
print(s.countTriplets(arr1))
t2 = datetime.now()
print(t2 - t1)
