#329
#找到矩阵内最长的递增路径，严格递增
#dp[i,j]为从i,j开始的最长路径
from collections import defaultdict
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = defaultdict(int)

        # 记忆化搜索
        def f1(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            # #越界
            # if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
            #     dp[(i,j)] = 0
            #     return 0
            # 四个方向搜索,单调就避免了回头的情况，不需要单独处理了
            up, down, left, right = 0, 0, 0, 0
            # 上
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                up = f1(i - 1, j)
            # 下
            if i + 1 <= len(matrix) - 1 and matrix[i + 1][j] > matrix[i][j]:
                down = f1(i + 1, j)
            # 右
            if j + 1 <= len(matrix[0]) - 1 and matrix[i][j + 1] > matrix[i][j]:
                left = f1(i, j + 1)
            # 左
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                right = f1(i, j - 1)
            dp[i, j] = max(up, down, left, right) + 1
            return dp[i, j]

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, f1(i, j))

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))