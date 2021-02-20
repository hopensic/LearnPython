from datetime import datetime
from typing import List

'''
tag: ^1641 ^medium ^math ^dp ^backtracking
name: ^(Count Sorted Vowel Strings)
'''


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5
        lst = [[0] * 6 for _ in range(n)]
        lst[0] = [1, 1, 1, 1, 1, 5]
        totalSum = 5
        for i in range(1, n):
            t1 = t2 = tempSum = totalSum
            for j in range(1, 5):
                tempSum -= lst[i - 1][j - 1]
                t1 += tempSum
                lst[i][j] = tempSum
            lst[i][0] = t2
            totalSum = lst[i][5] = t1

        return lst[-1][-1]


n = 1

t1 = datetime.now()
s = Solution()
print(s.countVowelStrings(n))
t2 = datetime.now()
print(t2 - t1)
