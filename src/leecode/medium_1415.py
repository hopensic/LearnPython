from datetime import datetime

'''
tag: ^1415 ^medium ^backtracking
name: ^(The k-th Lexicographical String of All Happy Strings of Length n)
'''


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        lst = [-1] * (n + 1)
        cur_k = 0
        tup = (0, 1, 2)
        dic = {0: 'a', 1: 'b', 2: 'c'}

        def make_string(last_position: int):
            nonlocal cur_k
            new_position = last_position + 1
            for i in tup:
                if i == lst[last_position]:
                    continue
                lst[new_position] = i
                if new_position < n:
                    if make_string(new_position) == k:
                        return cur_k
                else:
                    cur_k += 1
                    #  res.append([lst[:]])
                    if cur_k == k:
                        return cur_k
            return cur_k

        if make_string(0) == k:
            return "".join([dic[tup[i]] for i in lst[1:]])
        else:
            return ""


n = 1
k = 4
t1 = datetime.now()
s = Solution()
print(s.getHappyString(n, k))
t2 = datetime.now()
print(t2 - t1)
