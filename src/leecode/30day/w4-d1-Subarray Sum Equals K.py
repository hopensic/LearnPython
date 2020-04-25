from collections import defaultdict
from datetime import datetime
import operator


class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        res = 0
        prefix_sum = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in nums:
            prefix_sum += i
            res += dic[prefix_sum - k]
            dic[prefix_sum] += 1
        return res


# shift = [1,2,1,-1,0,3]
shift = [2]
k = 2
t1 = datetime.now()
s = Solution()
print(s.subarraySum(shift, k))
t2 = datetime.now()
print(t2 - t1)
