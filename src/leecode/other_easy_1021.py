class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        p = []
        num = 0
        isBegin = True
        for c in S:
            if num == 0:
                isBegin = True
            else:
                isBegin = False
            if (c == '('):
                num += 1
            else:
                num -= 1
            if num != 0 and (not isBegin):
                p.append(c)

        return ''.join(p)


ss = "()()"

s = Solution()
print(s.removeOuterParentheses(ss))
