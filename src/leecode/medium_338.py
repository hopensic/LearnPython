from datetime import datetime

'''
tag: ^338 ^medium ^dp ^bit manipulation
name: ^(Counting Bits)
'''


class Solution:
    def countBits(self, num: int) -> list:
        res = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                res.append(res[int(i / 2)])
            else:
                res.append(1 + res[int(i - 1 / 2)])

        return res


t1 = datetime.now()
s = Solution()
print(s.countBits(17))
t2 = datetime.now()
print(t2 - t1)
