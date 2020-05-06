from datetime import datetime
from typing import List

'''
tag: ^1357 ^medium ^design
name: ^(Apply Discount Every n Orders)
'''


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.c = 0
        self.dic = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.c += 1
        total = sum([self.dic[product[i]] * amount[i] for i in range(len(product))])
        if self.c % self.n == 0:
            total *= 1 - self.discount / 100
        return total


cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
print(cashier.getBill([1, 2], [1, 2]))
print(cashier.getBill([3, 7], [10, 10]))
print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
