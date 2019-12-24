from datetime import datetime
from collections import Counter

'''
tag: ^766 ^easy ^array ^sort
name: ^(Element Appearing More Than 25% In Sorted Array)
'''


class Solution:
    def findSpecialInteger(self, arr) -> int:
        return Counter(arr).most_common()[0][0]



arr1 = [1,2,2,6,6,6,6,7,10]

t1 = datetime.now()
s = Solution()
print(s.findSpecialInteger(arr1))
t2 = datetime.now()
print(t2 - t1)
