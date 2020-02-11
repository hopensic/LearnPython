from datetime import datetime

'''
tag: ^1342 ^easy ^bit-manipulation
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            num = num / 2 if num % 2 == 0 else num - 1
            res += 1
        return res


arr1 = 123

t1 = datetime.now()
s = Solution()
print(s.numberOfSteps(arr1))
t2 = datetime.now()
print(t2 - t1)
