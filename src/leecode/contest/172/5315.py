class Solution:
    def maximum69Number(self, num: int) -> int:
        j = str(num)
        z = j.replace('6', '9', 1)
        return int(z)


s = Solution()
print(s.maximum69Number(999))
