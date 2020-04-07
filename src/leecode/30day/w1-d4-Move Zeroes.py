from datetime import datetime


class Solution:
    def moveZeroes(self, nums: list) -> None:
        if len(nums) < 2:
            return
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for idx, i in enumerate(nums):
            if i == 0:
                n += 1
            else:
                if n > 0:
                    nums[idx - n] = i

        for i in range(1, n + 1):
            nums[(-1) * i] = 0
        print(nums)


arr1 = [0, 1, 2, 0, 0,1,1,0, 4, 5, 0, 3, 12, 1]
# arr1 = [0, 1, 2, 0, 0, 4, 5, 0, 3, 12, 1]

t1 = datetime.now()
s = Solution()
print(s.moveZeroes(arr1))
t2 = datetime.now()
print(t2 - t1)
