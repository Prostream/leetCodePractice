#200 判断一个邻阶矩阵里有多少个岛
# 可以理解成连通性问题，用DFS或者BSF可以解决
# 把访问过的地方置0，可以省点空间
#
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        nums = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:#越界了
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'#访问过的地方置为0

                #四个方向探索
                dfs(row,col-1)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row+1,col)
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    nums += 1
                    dfs(row,col)
        return nums