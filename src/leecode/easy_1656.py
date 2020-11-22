from datetime import datetime
from typing import List

'''
tag: ^1656 ^easy ^array ^design
name: ^(Design an Ordered Stream)
'''


class OrderedStream:

    def __init__(self, n: int):
        self.num = n
        self.lst = [None] * n
        self.next = 1
        self.dic = {k: None for k in range(1, n + 1)}

    def insert(self, id: int, value: str) -> List[str]:
        res = []
        self.dic[id] = value
        if self.next == id:
            tmp = self.next
            while self.dic.get(tmp):
                res.append(self.dic.get(tmp))
                tmp += 1
            self.next = tmp
        return res


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
print(obj.insert(3, 'c'))
print(obj.insert(1, 'a'))
print(obj.insert(2, ''))

# param_1 = obj.insert(id,value)
