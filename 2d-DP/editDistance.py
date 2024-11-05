#72
#编辑距离问题
#word1变化为word2，插入代价a，删除代价b，替换代价c,这里是一种特例，都是1
#
from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = defaultdict(int)
        #从底到顶
        #word1前i长度，word2前j长度，代价最低的替换代价
        #[0...i-1] [0...j-1]
        #1.i-1参与，负责j-1，且本来就相等，不增加代价
        #2.i-1参与，负责j-1，不相等，替换代价
        #3.i-1参与，不负责j-1，dp[i,j-1]，插入代价
        #4.i-1不参与，dp[i-1,j]，删除代价
        def f1():
            #边界都做好
            for j in range(len(word2)+1):
                dp[(0,j)] = j
            for i in range(1,len(word1)+1):
                dp[(i,0)] = i
            for i in range(1,len(word1)+1):
                for j in range(1, len(word2)+1):
                    min_cost = float('inf')
                    #1
                    if word1[i-1] == word2[j-1]:
                        min_cost = min(dp[(i-1,j-1)], min_cost)
                    #2
                    min_cost = min(dp[(i-1,j-1)]+1, min_cost)
                    #3
                    min_cost = min(dp[(i,j-1)+1], min_cost)
                    #4
                    min_cost = min(dp[(i-1,j)]+1, min_cost)
                    dp[(i,j)] = min_cost

            return dp[(len(word1),len(word2))]

        def f2():


        return f1()