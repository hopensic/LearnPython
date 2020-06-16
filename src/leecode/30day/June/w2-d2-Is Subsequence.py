from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0 and m == 0:
            return True
        else:
            if m == 0: return False
            if n == 0: True

        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if t[i] == s[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
            if dp[n] == n:
                return True
        return False


s = "axc"
t = "ahbabgdc"
s1 = Solution()
print(s1.isSubsequence(s, t))
