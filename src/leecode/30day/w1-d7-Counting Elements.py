from collections import Counter
from _collections import defaultdict
from datetime import datetime


class Solution:
    def countElements(self, arr: list) -> int:
        set1 = set(arr)
        c = Counter([i + 1 for i in arr])
        res = sum(v for k, v in c.items() if k in set1)
        return res


arr1 = [1, 3, 2, 3, 5, 0]
t1 = datetime.now()
s = Solution()
print(s.countElements(arr1))
t2 = datetime.now()
print(t2 - t1)
