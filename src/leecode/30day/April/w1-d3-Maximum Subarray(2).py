from datetime import datetime


class Solution:
    def maxSubArray(self, nums: list) -> int:
        gbl, local = [nums[0]], [nums[0]]
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            local.append(max(nums[i], nums[i] + local[i - 1]))
            gbl.append(max(gbl[i - 1], local[i]))
        return gbl[-1]


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

t1 = datetime.now()
s = Solution()
print(s.maxSubArray(arr1))
t2 = datetime.now()
print(t2 - t1)
