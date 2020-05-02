from datetime import datetime


class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) < 2:
            return 0
        sums = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                sums += prices[i + 1] - prices[i]
        return sums


arr1 = [7, 1, 5, 3, 6, 4]

t1 = datetime.now()
s = Solution()
print(s.maxProfit(arr1))
t2 = datetime.now()
print(t2 - t1)
