class Solution:
    def minTimeToVisitAllPoints(self, points):
        le = len(points)
        if le == 1:
            return 0
        ret = 0
        for i in range(le - 1):
            x, y = abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1])
            ret += min(x, y) + abs(x - y)
        return ret


lst = [[431, 91], [838, -127]]
s = Solution()
print(s.minTimeToVisitAllPoints(lst))
