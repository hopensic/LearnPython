from datetime import datetime

'''
tag: ^986 ^medium ^two-pointers
name: ^(Interval List Intersections)
'''


class Solution:
    def intervalIntersection(self, A, B):
        m, n = len(A), len(B)
        if m == 0 or n == 0:
            return []
        res = []
        i, j = 0, 0
        while i < m and j < n:


            interval1 = A[i]
            interval2 = B[j]
            if interval1[0] == interval2[0]:
                if interval1[1] <= interval2[1]:
                    res.append([interval1[0], interval1[1]])
                    i += 1
                    if interval1[1] == interval2[1]:
                        j += 1
                else:
                    res.append([interval1[0], interval2[1]])
                    j += 1
            elif interval1[0] < interval2[0]:
                if interval1[1] <= interval2[0]:
                    i += 1
                    if interval1[1] == interval2[0]:
                        res.append([interval2[0], interval2[0]])
                else:
                    if interval1[1] >= interval2[1]:
                        j += 1
                        res.append([interval2[0], interval2[1]])
                        if interval1[1] == interval2[1]:
                            i += 1
                    else:
                        res.append([interval2[0], interval1[1]])
                        i += 1
            else:
                if interval1[0] >= interval2[1]:
                    j += 1
                    if interval1[0] == interval2[1]:
                        res.append([interval1[0], interval1[0]])
                else:
                    if interval1[1] <= interval2[1]:
                        i += 1
                        res.append([interval1[0], interval1[1]])
                        if interval1[1] == interval2[1]:
                            j += 1
                    else:
                        res.append([interval1[0], interval2[1]])
                        j += 1

        return res


# A1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
# B1 = [[1, 5], [8, 12], [15, 24], [25, 26]]
A1 = [[4, 6], [7, 8], [10, 17]]
B1 = [[5, 10]]

t1 = datetime.now()
s = Solution()
print(s.intervalIntersection(A1, B1))
t2 = datetime.now()
print(t2 - t1)
