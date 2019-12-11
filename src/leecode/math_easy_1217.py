class Solution:
    def minCostToMoveChips(self, chips):
        return min([sum((chip - position) % 2 for chip in chips if chip != position) for position in set(chips)])


chips = [2, 2, 2, 3, 3]
# chips = [1, 2, 3]
s = Solution()
print(s.minCostToMoveChips(chips))
