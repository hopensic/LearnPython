class Solution:
    def arrayPairSum(self, nums: list) -> int:
        return sum(sorted(nums)[0::2])


lst = [1,4,2,3]

s = Solution()
print(s.arrayPairSum(lst))
