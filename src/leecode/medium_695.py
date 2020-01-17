from datetime import datetime

'''
tag: ^695 ^medium ^array ^dfs
name: ^(Max Area of Island)
'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        M = len(grid)
        N = len(grid[0])
        print('M=' + str(M))
        print('N=' + str(N))

        pos_grid = [[[(0, 1), (-1, 0), (0, -1), (1, 0)] for j in range(N)] for i in range(M)]
        max_area = 0
        stacks = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 or grid[i][j] == -1:
                    continue
                temp_area = 1
                cur_pos = (j, i)
                grid[i][j] = -1
                stacks.append(cur_pos)
                while len(stacks) > 0:
                    x, y = stacks[-1]
                    while len(pos_grid[y][x]) > 0:
                        direction = pos_grid[y][x].pop()
                        new_pos = x + direction[0], y + direction[1]
                        new_x, new_y = new_pos
                        # 超出边界
                        if new_x < 0 or new_x > N - 1:
                            continue
                        if new_y < 0 or new_y > M - 1:
                            continue
                        # 该位置是水，或者已经设置过(已探寻过的位置将会设成-1)
                        if grid[new_y][new_x] == 0 or grid[new_y][new_x] == -1:
                            continue
                        # 是1的话，就要将面积加1
                        else:
                            temp_area += 1
                            stacks.append((new_x, new_y))
                            grid[new_y][new_x] = -1
                            # x, y = new_x, new_y
                            # max_area = max(max_area, temp_area)
                            break
                    else:
                        poped = stacks.pop()
                        grid[poped[1]][poped[0]] = -1
                max_area = max(max_area, temp_area)
        return max_area


arr1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

t1 = datetime.now()
s = Solution()
print(s.maxAreaOfIsland(arr1))
t2 = datetime.now()
print(t2 - t1)
