import unittest


class Solution:
    def numRookCaptures(self, board):
        num = 0
        is_find = False
        le = len(board)
        rx, ry = 0, 0
        for i in range(le):
            for j in range(le):
                if board[i][j] == 'R':
                    rx, ry = i, j
                    is_find = True
                    break
            if is_find:
                break

        if ry > 0:
            for x in board[rx][:ry][::-1]:
                if x == 'p':
                    num += 1
                    break
                if x == 'B':
                    break;

        if ry < le:
            for x in board[rx][ry + 1:]:
                if x == 'p':
                    num += 1
                    break
                if x == 'B':
                    break;

        lst = list(range(le))
        if rx > 0:
            for xx in lst[:rx][::-1]:
                if board[xx][ry] == 'p':
                    num += 1
                    break
                if board[xx][ry] == 'B':
                    break
        if rx < le:
            for xx in lst[rx + 1:]:
                if board[xx][ry] == 'p':
                    num += 1
                    break
                if board[xx][ry] == 'B':
                    break;
        return num


input1 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

input2 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

input3 = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

s = Solution()
print(s.numRookCaptures(input1))


class TestCase999(unittest.TestCase):

    def test_abc(self):
        self.assertEqual(3, s.numRookCaptures(input1))
        self.assertEqual(0, s.numRookCaptures(input2))
        self.assertEqual(3, s.numRookCaptures(input3))


if __name__ == '__main__':
    unittest.main()
