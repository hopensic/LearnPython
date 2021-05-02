from collections import Counter
from datetime import datetime
from typing import List

'''
tag: ^1832 ^easy ^string
name: ^(Check if the Sentence Is Pangram)
'''


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(Counter(sentence)) == 26 else False


sentence = "thequickbrownfoxjumpsoverthelazydog"

t1 = datetime.now()
s = Solution()
print(s.checkIfPangram(sentence))
t2 = datetime.now()
print(t2 - t1)
