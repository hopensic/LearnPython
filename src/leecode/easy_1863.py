from datetime import datetime
from typing import List

'''
tag: ^1863 ^easy ^array ^backtracking ^bit-manipulation
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        le = len(nums)
        res = 0
        def test(curIdx: int, cur_value: int):
            nonlocal res
            for j in range(curIdx, le):
                tmp = cur_value ^ nums[j]
                res += tmp
                test(j + 1, tmp)
            return
        test(0, 0)
        return res


arr1 = [3,4,5,6,7,8]

t1 = datetime.now()
s = Solution()
print(s.subsetXORSum(arr1))
t2 = datetime.now()
print(t2 - t1)
