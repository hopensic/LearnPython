from datetime import datetime
from collections import deque

'''
tag: ^1284 ^hard ^bfs
name: ^(Minimum Number of Flips to Convert Binary Matrix to Zero Matrix)
'''


class Solution:
    def minFlips(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        original = []
        for lst in mat:
            original.extend([str(x) for x in lst])
        lst = deque()
        lst.append(int('0b' + ''.join(original), 2))
        seen = set()
        steps = 0
        expend = set()
        while len(lst) > 0:
            cur_size = len(lst)
            for i in range(cur_size):
                poped = lst.pop()
                if poped == 0:
                    return steps
                # 求出扩展
                expend.clear()
                t = m * n
                for i in range(t):
                    temp = poped
                    # 翻转4个方向的
                    if i % n - 1 > -1:
                        temp ^= 1 << t - (i - 1) - 1
                    if i % n + 1 < n:
                        temp ^= 1 << t - (i + 1) - 1
                    if i - n > -1:
                        temp ^= 1 << t - (i - n) - 1
                    if i + n < t:
                        temp ^= 1 << t - (i + n) - 1
                    # 翻转自己
                    temp ^= 1 << t - i - 1
                    expend.add(temp)
                for e in expend:
                    if e not in seen:
                        lst.appendleft(e)
                        seen.add(e)
            steps += 1
        return -1


# arr1 = [[1, 1, 1], [0, 1, 0]]
arr1 = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]

t1 = datetime.now()
s = Solution()
print(s.minFlips(arr1))
t2 = datetime.now()
print(t2 - t1)
