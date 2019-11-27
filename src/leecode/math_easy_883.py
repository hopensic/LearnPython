class Solution:
    def projectionArea(self, grid) -> int:
        top = sum(x > 0 for lst in grid for x in lst)
        side = sum(max(lst) for lst in grid)
        front = sum(max(tup) for tup in zip(*g))
        return top + side + front


g = [[4, 1, 3], [3, 0, 2], [2, 4, 5]]
s = Solution()
print(s.projectionArea(g))
