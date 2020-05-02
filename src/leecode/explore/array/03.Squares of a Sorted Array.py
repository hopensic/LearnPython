class Solution:
    def sortedSquares(self, A: list) -> list:
        return sorted([i ** 2 for i in A])


arr = [555, 901, 482, 1771]
solution = Solution()
print(solution.findNumbers(arr))
