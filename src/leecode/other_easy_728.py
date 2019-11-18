class Solution:

    def test(self, num):
        s = str(num)
        for x in s:
            if x == '0':
                return False
            if num % int(x) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int):
        lst = []
        for x in range(left, right + 1):
            if (self.test(x)): lst.append(x)
        return lst


so = Solution()
print(so.selfDividingNumbers(1, 22))
