from random import randint


class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dic = {}
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.lst.append(val)
            self.dic[val] = len(self.lst)
            return True
        else:
            return False
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        if val != self.lst[-1]:
            self.dic[self.lst[-1]] = self.dic[val]
            self.lst[self.dic[val] - 1], self.lst[-1] = self.lst[-1],self.lst[self.dic[val] - 1]
        del self.dic[val]
        self.lst.pop()
        return True

        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.lst[randint(0, len(self.lst) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(2)
# param_2 = obj.remove(2)
param_3 = obj.insert(3)
param_3 = obj.insert(4)
param_3 = obj.insert(5)
param_4 = obj.remove(3)
param_5 = obj.getRandom()
print(1)
