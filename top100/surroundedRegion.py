#130
#围棋，需要把被吃的部分吃掉，我考虑还是DFS，然后用一个tuple的list存好这次联通图的位置信息，
# 然后遍历完看看这次的连通图是不是被完全包围的，如果是，就把记录的位置的值变为x，如果不是就只标记成已访问
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])


        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = '#'
            #四个方向
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        #边界的连通图全部变成#
        #1-1-1
        #1-1-1
        #1-1-1
        for row in [0, rows-1]:
            for col in range(cols):
                if board[row][col] == 'O':
                    dfs(row,col)
        for col in [0, cols-1]:
            for row in range(rows):
                if board[row][col] == 'O':
                    dfs(row,col)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '0':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return board