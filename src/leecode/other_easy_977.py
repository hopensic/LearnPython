class Solution:
    def sortedSquares(self, A):
        return sorted(x ** 2 for x in sorted(lst))


lst = [-7, -3, 2, 3, 11]
s = Solution()
print(s.sortedSquares(lst))
