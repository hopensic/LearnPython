class Solution:
    def removePalindromeSub(self, s: str) -> int:
        le = len(s)
        if le <= 1:
            return le


a = "ababa"

s = Solution()
print(s.removePalindromeSub(a))
