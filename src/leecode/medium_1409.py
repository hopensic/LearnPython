from datetime import datetime

'''
tag: ^1409 ^medium ^array
name: ^(Queries on a Permutation With Key)
'''


class Solution:
    def processQueries(self, queries: list, m: int) -> list:
        if m == 1:
            return [0]
        dic = {k + 1: k for k in range(m)}
        res = []
        for i in queries:
            res.append(dic[i])
            # 需要置换到起始位置的
            for k, v in dic.items():
                if v < res[-1]:
                    dic[k] += 1
            dic[i] = 0
        return res


queries = [7, 5, 5, 8, 3]
m = 8

t1 = datetime.now()
s = Solution()
print(s.processQueries(queries, m))
t2 = datetime.now()
print(t2 - t1)
