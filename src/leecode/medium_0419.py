from datetime import datetime

'''
tag: ^0419 ^medium ^
name: ^(Battleships in a Board)
'''


class Solution:
    def countBattleships(self, board) -> int:
        m, n = len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                else:
                    if i == 0 and j == 0:
                        if board[i][j] == 'X':
                            res += 1
                    elif i == 0 and j > 0:
                        if board[i][j - 1] == '.':
                            res += 1
                    elif i > 0 and j == 0:
                        if board[i - 1][j] == '.':
                            res += 1
                    else:
                        if board[i - 1][j] == '.' and board[i][j - 1] == '.':
                            res += 1

        return res


arr1 = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]

t1 = datetime.now()
s = Solution()
print(s.countBattleships(arr1))
t2 = datetime.now()
print(t2 - t1)
