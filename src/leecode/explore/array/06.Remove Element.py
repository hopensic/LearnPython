from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position_val = len(nums) - 1
        num_of_val = 0
        for i in range(position_val, -1, -1):
            if nums[i] == val:
                nums[i], nums[position_val] = nums[position_val], nums[i]
                position_val -= 1
                num_of_val += 1
        return len(nums) - num_of_val


nums = [1,1,2,2,1]
val = 2
solution = Solution()
print(solution.removeElement(nums, val))
