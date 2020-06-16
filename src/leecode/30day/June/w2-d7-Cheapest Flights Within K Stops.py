from collections import defaultdict, deque
from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, destination: int, K: int) -> int:
        # bfs solution
        queue = deque()
        queue.append((source, 0))
        steps = 0
        dic = defaultdict(dict)
        lowest_cost = float("inf")
        # init graph
        for src, dst, cost in flights:
            dic[src][dst] = cost

        while len(queue) > 0:
            le = len(queue)
            while le > 0:
                le -= 1
                cur, cost = queue.popleft()
                if cur == destination:
                    lowest_cost = min(lowest_cost, cost)
                for neibour, neibour_cost in dic[cur].items():
                    if cost + neibour_cost > lowest_cost:
                        continue
                    queue.append((neibour, cost + neibour_cost))
            steps += 1
            if steps > K + 1:
                break
        return -1 if lowest_cost == float("inf") else lowest_cost


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
source = 0
destination = 2
k = 0
# nums = [2, 3, 8, 9, 27]
# nums = [1,2,4,8]
# nums = [4, 8, 10, 240]
# nums = [546, 669]
s1 = Solution()
print(s1.findCheapestPrice(n, edges, source, destination, k))
