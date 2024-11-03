#64
#grid里从左上到右下的最小路径和
#动态规划
from collections import defaultdict
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        row = []
        # 暴力递归
        # 在i,j位置的表依赖i-1,j位置，i,j-1位置
        def f0(i, j):
            # 第一个格子
            if i == 0 and j == 0:
                return grid[0][0]
            up = float('inf')
            left = float('inf')
            if i - 1 >= 0:
                up = grid[i][j] + f0(i - 1, j)
            if j - 1 >= 0:
                left = grid[i][j] + f0(i, j - 1)
            return min(up, left)

        # 记忆化搜索
        def f1(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            # 第一个格子
            if i == 0 and j == 0:
                dp[(0, 0)] = grid[0][0]
                return grid[0][0]
            up = float('inf')
            left = float('inf')
            if i - 1 >= 0:
                up = grid[i][j] + f1(i - 1, j)
            if j - 1 >= 0:
                left = grid[i][j] + f1(i, j - 1)
            dp[(i, j)] = min(up, left)
            return min(up, left)

        # 从底到顶
        def f2():
            # 第一个格子
            dp[(0, 0)] = grid[0][0]
            #最左边和最上面准备好
            for j in range(1, len(grid[0])):
                dp[(0, j)] = dp[(0,j-1)] + grid[0][j]
            for i in range(1, len(grid)):
                dp[(i,0)] = dp[(i-1,0)] + grid[i][0]
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])):
                    up = grid[i][j] + dp[(i-1, j)]
                    left = grid[i][j] + dp[(i, j-1)]
                    dp[(i,j)] = min(up, left)
            return dp[(len(grid) - 1, len(grid[0]) - 1)]

        # 只用一行dp来处理
        def f3():
            # 第一个格子
            row[0] = grid[0][0]
            #准备好第一行
            for i in range(1, len(grid[0])):
                row[i] = row[i-1] + grid[0][i]

            #第二行开始
            for j in range(1, len(grid[0])):
                #对row的每个元素进行处理
                row[0] = row[0] + grid[0][j]
                for i in range(1, len(row)):
                    row[i] = min(row[i-1],row[i]) + grid[j][i]

            return row[len(row) - 1]

        # return f0(len(grid)-1, len(grid[0])-1)
        return f1(len(grid) - 1, len(grid[0]) - 1)