from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: list):
        self.ordered_dic = OrderedDict()
        self.duplicated_set = set()
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        lst1 = list(self.ordered_dic.keys())
        return lst1[0] if len(lst1) > 0 else -1

    def add(self, value: int) -> None:
        if value not in self.duplicated_set:
            if self.ordered_dic.get(value, 0) == 0:
                self.ordered_dic[value] = 1
            else:
                del self.ordered_dic[value]
                self.duplicated_set.add(value)


lst = [2, 3, 5]
firstUnique = FirstUnique(lst)
print(firstUnique.showFirstUnique())
firstUnique.add(5)
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())
