class Solution:
    def sumZero(self, n: int):
        lst = []
        if n % 2 == 1:
            lst.append(0)
        for i in range(1, int(n / 2) + 1):
            lst.append(i)
            lst.append((-1) * i)

        return lst


s = Solution()
print(s.sumZero(1))
