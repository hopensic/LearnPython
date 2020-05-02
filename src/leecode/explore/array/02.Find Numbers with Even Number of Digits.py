class Solution:
    def findNumbers(self, nums: list) -> int:
        return len([s for s in nums if len(str(s)) % 2 == 0])


arr = [555, 901, 482, 1771]
solution = Solution()
print(solution.findNumbers(arr))
