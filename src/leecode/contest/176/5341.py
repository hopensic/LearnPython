class ProductOfNumbers:

    def __init__(self):
        self.total = 1
        self.lst = []
        self.lst_withoutz = []

    def add(self, num: int) -> None:
        self.total *= (1 if num == 0 else num)
        self.lst.append(num)
        self.lst_withoutz.append(self.total)

    def getProduct(self, k: int) -> int:
        if self.lst[-k:].count(0) > 0:
            return 0
        if k == 1:
            return self.lst[-1]
        if k == len(self.lst_withoutz):
            return self.lst_withoutz[-1]
        return int(self.lst_withoutz[-1] / self.lst_withoutz[len(self.lst_withoutz) - k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(0)
obj.add(0)
obj.add(9)
param_1 = obj.getProduct(3)
obj.add(8)
obj.add(3)
obj.add(8)
param_2 = obj.getProduct(5)
param_3 = obj.getProduct(4)
param_4 = obj.getProduct(6)

print(param_1)
print(param_2)
print(param_3)
print(param_4)
