from datetime import datetime

'''
tag: ^349 ^easy ^hash-table ^two-pointers ^binary-search ^sort
name: ^(Intersection of Two Arrays)
'''


class Solution:
    def intersection(self, nums1, nums2) :
        return list(set(nums1).intersection(set(nums2)))











nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

t1 = datetime.now()
s = Solution()
print(s.intersection(nums1,nums2))
t2 = datetime.now()
print(t2 - t1)
