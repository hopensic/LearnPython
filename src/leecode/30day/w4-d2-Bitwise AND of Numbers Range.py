from collections import defaultdict
from datetime import datetime
import bisect


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        lst = [0, 1]
        tmp = 1
        for i in range(1, 32):
            tmp <<= 1
            lst.append(tmp)
        print(lst)
        # 判断m和n是否属于同一个区间
        left_index = bisect.bisect(lst, m) - 1
        right_index = bisect.bisect(lst, n) - 1

        sums = 0
        while left_index == right_index:
            sums += lst[left_index]
            m -= lst[left_index]
            n -= lst[right_index]
            m_index = bisect.bisect(lst, m) - 1
            n_index = bisect.bisect(lst, n) - 1
            left_index = min(m_index, n_index)
            right_index = max(m_index, n_index)
        return sums


m, n = 0, 0
t1 = datetime.now()
s = Solution()
print(s.rangeBitwiseAnd(m, n))
t2 = datetime.now()
print(t2 - t1)
