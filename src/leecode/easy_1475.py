from datetime import datetime
from typing import List

'''
tag: ^1475 ^easy ^array
name: ^(Final Prices With a Special Discount in a Shop)
'''


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack[-1]] -= price
                stack.pop()
            stack.append(idx)
        return prices


# prices = [5, 4, 10, 2, 6, 1, 1, 1, 9, 1]
prices = [8, 7, 4, 2, 8, 1, 7, 7, 10, 1]
# prices = [8, 4, 6, 2, 3]

t1 = datetime.now()
s = Solution()
print(s.finalPrices(prices))
t2 = datetime.now()
print(t2 - t1)
