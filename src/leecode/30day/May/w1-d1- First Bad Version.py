from collections import Counter
from datetime import datetime


class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n-1
        dic = {}
        dic[0] = False
        dic[1] = False
        dic[2] = False
        dic[3] = False
        dic[4] = True
        dic[5] = True
        dic[6] = True

        def isBadVersion(x):
            return dic[x]

        while left <= right:
            mid = left+int((right-left)/2)
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid+1
        return left+1


n = 5
t1 = datetime.now()
s = Solution()
print(s.firstBadVersion(n))
t2 = datetime.now()
print(t2 - t1)
