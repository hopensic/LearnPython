from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        for k, v in c2.items():
            tmp = c1[k]
            if tmp == 0:
                continue
            tmp -= v
            if tmp < 0:
                tmp = 0
            c1[k] = tmp
        return sum(v for v in c1.values())


s = "friend"
t = "family"

ss = Solution()
print(ss.minSteps(s, t))
