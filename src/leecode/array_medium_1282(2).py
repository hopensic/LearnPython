from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes):
        count = defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s] for s, l in count.items() for i in range(0, len(l), s)]


lst = [3, 3, 3, 3, 3, 1, 3]
s = Solution()
print(s.groupThePeople(lst))
