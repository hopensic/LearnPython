class StockSpanner:

    def __init__(self):
        self.stacks = []

    def next(self, price: int) -> int:
        n = 1
        while self.stacks:
            val, num = self.stacks[-1]
            if price < val:
                self.stacks.append((price, n))
                return n
            else:
                n += num
                self.stacks.pop()
        self.stacks.append((price, n))
        return n


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
param_1 = obj.next(60)
param_1 = obj.next(70)
param_1 = obj.next(60)
param_1 = obj.next(75)
param_1 = obj.next(85)
