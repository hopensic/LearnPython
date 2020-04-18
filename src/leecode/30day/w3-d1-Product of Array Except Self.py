from datetime import datetime
import operator
from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums: list) -> list:
        # 先计算nums[i]左边的乘积
        prod = 1
        res = [prod]
        for i in range(len(nums) - 1):
            prod *= nums[i]
            res.append(prod)
        # 再计算nums[i]右边的乘积
        prod = 1
        for i in range(-1, -len(nums), -1):
            prod *= nums[i]
            res[i - 1] *= prod
        return res


shift = [2, 3, 4, 5]
t1 = datetime.now()
s = Solution()
print(s.productExceptSelf(shift))
t2 = datetime.now()
print(t2 - t1)
