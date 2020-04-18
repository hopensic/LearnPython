from datetime import datetime

'''
tag: ^1395 ^medium ^array
name: ^(Count Number of Teams)
'''


class Solution:
    def numTeams(self, rating: list) -> int:
        le = len(rating)
        if le < 3:
            return 0
        res = 0
        for i in range(le):
            for j in range(i + 1, le):
                for k in range(j + 1, le):
                    if (rating[i] < rating[j] < rating[k] or
                            rating[i] > rating[j] > rating[k]):
                        res += 1

        return res


arr1 = [1, 3, 2, 9, 7, 5, 6]

t1 = datetime.now()
s = Solution()
print(s.numTeams(arr1))
t2 = datetime.now()
print(t2 - t1)
