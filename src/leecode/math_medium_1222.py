class Solution:
    def queensAttacktheKing(self, queens, king):
        N = 8

        a = set()
        for tup in [tuple(lst) for lst in queens]:
            a.add(tup)
        y, x = king
        ret_lst = []

        '''
         从king的位置向右搜搜索
         1.正右
         2.右上
         3.右下
        '''
        # 正右
        for x_axis in range(x + 1, N):
            if (y, x_axis) in a:
                ret_lst.append((y, x_axis))
                break
        # 右上
        temp_y = y
        for x_axis in range(N + 1, N):
            temp_y -= 1
            if (temp_y, x_axis) in a:
                ret_lst.append((temp_y, x_axis))
                break
        # 右下
        temp_y = y
        for x_axis in range(x + 1, N):
            temp_y += 1
            if (temp_y, x_axis) in a:
                ret_lst.append((temp_y, x_axis))
                break

        '''
        从king的位置向左搜搜索
        1.正右
        2.右上
        3.右下
        '''
        # 正左
        for x_axis in range(x - 1, -1, -1):
            if (y, x_axis) in a:
                ret_lst.append((y, x_axis))
                break
        # 左上
        temp_y = y
        for x_axis in range(x - 1, -1, -1):
            temp_y -= 1
            if (temp_y, x_axis) in a:
                ret_lst.append((temp_y, x_axis))
                break
        # 左下
        temp_y = y
        for x_axis in range(x - 1, -1, -1):
            temp_y += 1
            if (temp_y, x_axis) in a:
                ret_lst.append((temp_y, x_axis))
                break

        '''
            从king的位置向上向下搜索
        '''
        # 向上
        for y_axis in range(y - 1, -1, -1):
            if (y_axis, x) in a:
                ret_lst.append((y_axis, x))
                break
        # 向下
        for y_axis in range(y + 1, N):
            if (y_axis, x) in a:
                ret_lst.append((y_axis, x))
                break

        return ret_lst


# queens2 = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
#            [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
#            [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]

# king2 = [3, 4]

queens2 = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
king2 = [0, 0]

s = Solution()
print(s.queensAttacktheKing(queens2, king2))
