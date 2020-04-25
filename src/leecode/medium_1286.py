from datetime import datetime

'''
tag: ^1286 ^medium ^design ^backtracking
name: ^(Iterator for Combination)
'''


class CombinationIterator:
    abc = 'abcdefghijklmnopqrstuvwxyz'

    def gen_fun(n):
        def test(nn):
            if nn > 0:
                print(nn)
                test(nn - 1)
            else:
                yield nn

        yield test(3)

    def __init__(self, characters: str, combinationLength: int):
        cons_dic = {i: CombinationIterator.abc[i] for i in range(26)}
        self.real_len = len(characters)
        self.combinationLength = combinationLength
        self.characters = characters
        self.lst = [i for i in range(self.real_len)]
        self.cur_lst = [i for i in range(combinationLength)]
        self.section_dic = {i: (i, i + self.real_len - combinationLength) for i in range(combinationLength)}

        self.is_generator = False
        self.gen = CombinationIterator.gen_fun(3)

    def next(self) -> str:
        if self.combinationLength > self.real_len:
            return None
        if self.is_generator:
            self.is_generator = False
            return self.value
        else:
            try:
                return next(self.gen)
            except StopIteration:
                # self.value = None
                return None

    def hasNext(self) -> bool:
        if self.combinationLength > self.real_len:
            return False
        if self.is_generator:
            return True
        else:
            try:
                g = next(self.gen)
                next(g)
                self.value = next(self.gen)
                self.is_generator = True
                return True
            except StopIteration:
                self.value = None
                self.is_generator = False
                return False


com = CombinationIterator("abcdef", 2)
print(com.hasNext())
print(com.next())

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
