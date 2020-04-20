from datetime import datetime

'''
tag: ^1403 ^easy ^greedy ^sort
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def minSubsequence(self, nums: list) -> list:
        nums.sort()
        _sum = sum(nums)
        res = []
        tmp = 0
        for i in nums[::-1]:
            tmp += i
            res.append(i)
            if tmp > _sum - tmp:
                break
        res.sort(reverse=True)
        return res


arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]
#arr1 = [4, 3, 10, 9, 8]
#arr1 = [4, 4, 7, 6, 7]

t1 = datetime.now()
s = Solution()
print(s.minSubsequence(arr1))
t2 = datetime.now()
print(t2 - t1)
