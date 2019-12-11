from itertools import zip_longest


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        ret_lst = []
        sp = text.split(' ')
        le = len(sp)
        if le < 3:
            return []
        else:
            sp2 = sp[1:]
            sp3 = sp[2:]
            for x, y, z in zip_longest(sp, sp2, sp3):
                if x == first and y == second_i and z is not None:
                    ret_lst.append(z)
        return ret_lst


text_i = "alice is a good a good girl she is a good student"
first_i = 'a'
second_i = 'good'


s = Solution()
print(s.findOcurrences(text_i, first_i, second_i))
