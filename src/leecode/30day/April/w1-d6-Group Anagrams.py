from collections import Counter
from _collections import defaultdict
from datetime import datetime


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        dic = defaultdict(list)
        for word in strs:
            c = tuple(sorted(Counter(word).items(), key=lambda item: item[0]))
            dic[c].append(word)
        res = []
        for v in dic.values():
            res.append(v)
        return res


arr1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

t1 = datetime.now()
s = Solution()
print(s.groupAnagrams(arr1))
t2 = datetime.now()
print(t2 - t1)
