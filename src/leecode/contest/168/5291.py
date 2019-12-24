class Solution:
    def findNumbers(self, nums: list) -> int:
        ret_lst = len([len(str(num)) for num in nums if len(str(num)) % 2 == 0])
        return ret_lst


lst = [12, 345, 2, 6, 7896]

s = Solution()
print(s.findNumbers(lst))
