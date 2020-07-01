from collections import defaultdict, deque
from typing import List
import heapq
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class TrieNode:
    def __init__(self, ch):
        self.wordset = set()
        self.ch = ch
        self.sublist = None

    def add_sublist(self):
        self.sublist = [TrieNode(-1) for _ in range(26)]

    def set_val(self, ch):
        self.ch = ch


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word: str) -> None:
        p = self.root
        for ch in word:
            k = ord(ch) - 97
            if not p.sublist:
                p.add_sublist()
            p.sublist[k].set_val(ch)
            p = p.sublist[k]
        p.wordset.add(word)


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        if len(words) == 0:
            return res

        m = len(board)
        if m == 0:
            return res
        if m == 1:
            w = ''.join(board[0])
            wr = ''.join(reversed(board[0]))
            for word in words:
                if w.find(word) > -1 or wr.find(word) > -1:
                    res.append(word)
            return res
        n = len(board[0])
        if n == 0:
            return res
        if n == 1:
            lst = [board[i][0] for i in range(m)]
            w = ''.join(lst)
            wr = ''.join(reversed(lst))
            for word in words:
                if w.find(word) > -1 or wr.find(word) > -1:
                    res.append(word)
            return res

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(i: int, j: int, t: 'Trie'):
            c = board[i][j]
            if (c == '#' or not t.sublist or t.sublist[ord(c) - 97].ch == -1): return
            t = t.sublist[ord(c) - 97]
            if (len(t.wordset) > 0):
                res.append(t.wordset.pop())

            board[i][j] = '#'
            if (i > 0): dfs(i - 1, j, t)
            if (j > 0): dfs(i, j - 1, t)
            if (i < m - 1): dfs(i + 1, j, t)
            if (j < n - 1): dfs(i, j + 1, t)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        return res


# board = [["o", "a", "a", "n"],
#          ["e", "t", "a", "e"],
#          ["i", "h", "k", "r"],
#          ["i", "f", "l", "v"]]
board = [["a", "b"]]
# words = ["oath", "pea", "eat", "rain"]
words = ["ba"]
so = Solution()
print(so.findWords(board, words))
