from datetime import datetime
from typing import List

'''
tag: ^1641 ^medium ^math ^dp ^backtracking
name: ^(Count Sorted Vowel Strings)
'''


class Solution:
    def countVowelStrings(self, n: int) -> int:
        lst = [[1, 2, 3]] + [[0] * 3 for _ in range(2)]

        a = [[1, 3]] + [[2, 4]]
        print(a)
        return lst


n = 2

t1 = datetime.now()
s = Solution()
print(s.countVowelStrings(n))
t2 = datetime.now()
print(t2 - t1)
