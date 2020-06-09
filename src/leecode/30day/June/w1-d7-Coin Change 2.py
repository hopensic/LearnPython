from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] += dp[j - i]
        return dp[amount]



amount = 5
coins = [1, 2, 5]
s = Solution()

a = set()
a.add(1)
a.add(2)

b = set()
b.add(2)
b.add(1)
b.add(3)

print(a == b)

print(s.change(amount, coins))
