from datetime import datetime

'''
tag: ^1313 ^easy
name: ^(Decompress Run-Length Encoded List)
'''


class Solution:
    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i + 1]] * nums[i])
        return res


arr1 = [1, 2, 3, 4]

t1 = datetime.now()
s = Solution()
print(s.decompressRLElist(arr1))
t2 = datetime.now()
print(t2 - t1)
