from collections import defaultdict
from typing import List
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


# trips = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
trips = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
so = Solution()
print(so.findItinerary(trips))
