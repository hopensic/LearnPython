from datetime import datetime
from typing import List

'''
tag: ^1684 ^easy ^string
name: ^(Count the Number of Consistent Strings)
'''


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set1 = set(allowed)
        return [len(set(d) - set1) for d in words].count(0)



allowed = "cad"
words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]

t1 = datetime.now()
s = Solution()
print(s.countConsistentStrings(allowed, words))
t2 = datetime.now()
print(t2 - t1)
