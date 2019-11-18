class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        end = int(len(s) / 2)
        flag = True
        for idx in range(end):
            if s[idx] != s[(idx + 1) * (-1)]:
                flag = False
                break
        return flag


solution = Solution()
print(solution.isPalindrome(12343241))
