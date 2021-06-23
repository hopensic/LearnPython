from datetime import datetime
from typing import List

'''
tag: ^1859 ^easy ^string ^sort
name: ^(Sorting the Sentence)
'''


class Solution:
    def sortSentence(self, s1: str) -> str:
        res = []
        dic = {int(word[-1]): word[:-1] for word in s1.split(' ')}
        le = len(dic)
        for i in range(1, le + 1):
            res.append(dic[i])

        return ' '.join(res)


s1 = "is2 sentence4 This1 a3"

t1 = datetime.now()
s = Solution()
print(s.sortSentence(s1))
t2 = datetime.now()
print(t2 - t1)
