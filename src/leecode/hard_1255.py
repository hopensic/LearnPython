from datetime import datetime
from collections import Counter

'''
tag: ^1255 ^hard ^Bit-Manipulation
name: ^(Maximum Score Words Formed by Letters)
'''


class Solution:
    def maxScoreWords(self, words: list, letters: list, score: list) -> int:
        wordscore_map = {}
        score_map = {}
        valid_word_list = []
        counter = Counter(letters)
        score_map = {chr(i + 97): score[i] for i in range(26)}
        for word in words:
            tmp_score = 0
            tmp_count = Counter(word)
            for k, v in tmp_count.items():
                if v <= counter[k]:
                    tmp_score += v * score_map[k]
                else:
                    break
            else:
                wordscore_map[word] = tmp_score
                valid_word_list.append(word)
        res = 0

        def dfs(idx, cur_score):
            nonlocal res
            nonlocal counter
            res = max(cur_score, res)
            for i in range(idx, len(valid_word_list)):
                w = valid_word_list[i]
                w_count = Counter(w)
                is_valid = True
                for k, v in w_count.items():
                    counter[k] -= v
                    is_valid &= counter[k] >= 0
                if is_valid:
                    dfs(i + 1, cur_score + wordscore_map[w])
                for k, v in w_count.items():
                    counter[k] += v

        dfs(0, 0)
        return res


# words = ["dog", "cat", "dad", "good"]
# letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
# score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

t1 = datetime.now()
s = Solution()
print(s.maxScoreWords(words, letters, score))
t2 = datetime.now()
print(t2 - t1)
