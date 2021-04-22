from datetime import datetime
from typing import List

'''
tag: ^1773 ^easy ^arry ^string
name: ^(Count Items Matching a Rule)
'''


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        dic = {"type": 0, "color": 1, "name": 2}
        for lst in items:
            if lst[dic[ruleKey]] == ruleValue:
                res += 1

        return res


items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"

t1 = datetime.now()
s = Solution()
print(s.countMatches(items, ruleKey, ruleValue))
t2 = datetime.now()
print(t2 - t1)
