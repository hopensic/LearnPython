from collections import Counter
from datetime import datetime


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for k, v in r.items():
            m[k] -= v
        for v in m.values():
            if v < 0:
                return False
        return True


ransomNote = "aa"
magazine = "ab"
t1 = datetime.now()
s = Solution()
print(s.canConstruct(ransomNote, magazine))
t2 = datetime.now()
print(t2 - t1)
