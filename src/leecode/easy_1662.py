from datetime import datetime
from typing import List

'''
tag: ^1662 ^easy ^string
name: ^(Check If Two String Arrays are Equivalent)
'''


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


word1 = ["ab", "c"]
word2 = ["a", "bc"]

t1 = datetime.now()
s = Solution()
print(s.arrayStringsAreEqual(word1, word2))
t2 = datetime.now()
print(t2 - t1)
