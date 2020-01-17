class Solution:
    def getNoZeroIntegers(self, n: int):
        for i in range(1, n):
            if str(i).find('0')==-1 and str(n - i).find('0')==-1:
                return [i, n - i]


n = 1010

s = Solution()
print(s.getNoZeroIntegers(n))
