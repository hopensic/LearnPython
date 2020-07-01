from collections import defaultdict, deque
from typing import List
import heapq
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = deque()

        def dfs(depparture):
            arrivals = graph_dic[depparture]
            while arrivals:
                dfs(heapq.heappop(arrivals))
            path.appendleft(depparture)

        graph_dic = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph_dic[src], dst)
        dfs("JFK")
        return list(path)


# trips = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
trips = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
so = Solution()
print(so.findItinerary(trips))
