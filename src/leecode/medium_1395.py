from datetime import datetime

'''
tag: ^1395 ^medium ^array
name: ^(Count Number of Teams)
'''


class Solution:
    def numTeams(self, rating: list) -> int:
        le = len(rating)
        if le<3:
            return 0


        increase_lst, decrease_lst = [[rating[0]]], [[rating[0]]]
        i_idx, d_idx = 0, 0
        for i in range(len(rating)-1):


        return


arr1 = [1, 3, 2, 9, 7, 5, 6]

t1 = datetime.now()
s = Solution()
print(s.findSpecialInteger(arr1))
t2 = datetime.now()
print(t2 - t1)
