from datetime import datetime
from typing import List

'''
tag: ^1704 ^easy ^string
name: ^(Determine if String Halves Are Alike)
'''


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        set1 = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        le = len(s) // 2
        left = right = 0
        for i in range(le):
            if s[i] in set1:
                left += 1
            if s[i + le] in set1:
                right += 1
        return left == right


s1 = "AbCdEfGh"

t1 = datetime.now()
s2 = Solution()
print(s2.halvesAreAlike(s1))
t2 = datetime.now()
print(t2 - t1)
