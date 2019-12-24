class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        num = 0
        ret = 0
        for ch in S:
            if ch == '(':
                num += 1
            else:
                num -= 1

            if num < 0:
                ret += 1
                num = 0

        return num + ret


string = '())'
s = Solution()
print(s.minAddToMakeValid(string))
