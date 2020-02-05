import operator
from datetime import datetime
from itertools import accumulate

'''
tag: ^1310 ^medium ^bit-manipulation
name: ^(XOR Queries of a Subarray)
'''


class Solution:
    def xorQueries(self, arr, queries):
        lst = list(accumulate(arr, operator.xor))
        res = []
        for q_arr in queries:
            q1 = q_arr[0]
            q2 = q_arr[1]
            if q1 == q2:
                res.append(arr[q1])
            elif q1 == 0:
                res.append(lst[q2])
            else:
                res.append(lst[q2] ^ lst[q1 - 1])

        return res


arr = [4, 8, 2, 10]
queries = [[2, 3], [1, 3], [0, 0], [0, 3]]

t1 = datetime.now()
s = Solution()
print(s.xorQueries(arr, queries))
t2 = datetime.now()
print(t2 - t1)
