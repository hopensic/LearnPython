from datetime import datetime
from typing import List

'''
tag: ^1768 ^easy ^string
name: ^(Merge Strings Alternately)
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        le1 = len(word1)
        le2 = len(word2)
        min_len = min(le1, le2)
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        if le1 > le2:
            for j in range(i + 1, le1):
                res.append(word1[j])
        if le2 > le1:
            for j in range(i + 1, le2):
                res.append(word2[j])

        return ''.join(res)


word1 = "abc"
word2 = "pqrdd"

t1 = datetime.now()
s = Solution()
print(s.mergeAlternately(word1, word2))
t2 = datetime.now()
print(t2 - t1)
