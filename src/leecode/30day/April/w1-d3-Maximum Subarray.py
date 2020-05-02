from datetime import datetime


class Solution:
    def maxSubArray(self, nums: list) -> int:
        gbl = []
        local = []

        if len(nums) == 1:
            return nums[0]

        gbl.append(nums[0])
        local.append(nums[0])

        for idx, i in enumerate(nums[1:]):
            local.append(max(i, i + local[idx]))
            gbl.append(max(gbl[idx], local[idx + 1]))
        return gbl[-1]


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

t1 = datetime.now()
s = Solution()
print(s.maxSubArray(arr1))
t2 = datetime.now()
print(t2 - t1)
