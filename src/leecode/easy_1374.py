from datetime import datetime

'''
tag: ^1374 ^easy ^string
name: ^(Generate a String With Characters That Have Odd Counts)
'''


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' + 'b' * (n - 1)
        else:
            return 'a' * n


arr1 = 4

t1 = datetime.now()
s = Solution()
print(s.generateTheString(arr1))
t2 = datetime.now()
print(t2 - t1)
