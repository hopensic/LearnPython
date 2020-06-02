from datetime import datetime
from typing import List

'''
tag: ^1455 ^easy ^string
name: ^(Check If a Word Occurs As a Prefix of Any Word in a Sentence)
'''


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        le = len(searchWord)
        for idx, word in enumerate(words):
            if word[0:le] == searchWord:
                return idx + 1
        return -1

sentence = "i love eating burger"
searchWord = "burg"

t1 = datetime.now()
s = Solution()
print(s.isPrefixOfWord(sentence, searchWord))
t2 = datetime.now()
print(t2 - t1)
