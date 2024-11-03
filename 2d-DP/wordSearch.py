#79
#一个典型的不适合用来动态规划的题，可变参数复杂就不合适
#因为决定一个状态的既有几个int参数，同时还有一个二维表现在路径已经被访问过的状况，改动态规划太复杂了
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #暴力递归
        def f0(board, i, j, word, k):
            if k == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] != word[k]:
                return False
            tmp = board[i][j]
            board[i][j] = '0'
            #四个方向尝试
            ans = f0(board, i-1, j, word, k+1) or f0(board, i+1, j, word, k+1) or f0(board, i, j-1, word, k+1) or f0(board, i, j+1, word, k+1)
            board[i][j] = tmp

            return ans

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                ans = f0(board, i, j, word, 0)
                if ans:
                    return True

        return False