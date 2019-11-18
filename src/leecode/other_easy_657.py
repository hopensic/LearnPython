class Solution:
    def judgeCircle(self, moves) -> bool:
        x = 0
        y = 0
        for s in moves:
            if s == 'U':
                y += 1
            elif s == 'D':
                y -= 1
            elif s == 'R':
                x += 1
            else:
                x -= 1
        return (x == 0 and y == 0)


arr = "UD"

so = Solution()
print(so.judgeCircle(arr))
