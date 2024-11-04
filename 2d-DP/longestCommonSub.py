#1143
#最长公共子序列问题
from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = defaultdict(int)
        row = [0]*len(text2)

        #暴力递归 表示前缀长len1，len2的最长公共子序列是多少
        def f0(len1, len2):
            if len1 == 0 or len2 == 0:
                return 0
            if text1[len1-1] == text2[len2-1]:
                return f0(len1-1, len2-1)+1
            else:
                return max(f0(len1-1, len2), f0(len1, len2-1))


        #记忆化搜索
        def f1(len1,len2):
            if (len1, len2) in dp:
                return dp[(len1, len2)]
            if len1 == 0 or len2 == 0:
                dp[(len1, len2)] = 0
                return 0
            if text1[len1-1] == text2[len2-1]:
                dp[(len1, len2)] = f1(len1-1, len2-1)+1
                return dp[(len1, len2)]
            else:
                dp[(len1, len2)] = max(f1(len1-1, len2), f1(len1, len2-1))
                return dp[(len1, len2)]

        #从底到顶，左上简单，右下复杂
        def f2():
            dp[(0,0)] = 0
            #i作为行,j作为列
            for len1 in range(1,len(text1)+1):
                for len2 in range(1,len(text2)+1):
                    if text1[len1 - 1] == text2[len2 - 1]:
                        dp[(len1, len2)] = dp[(len1 - 1, len2 - 1)] + 1
                    else:
                        dp[(len1, len2)] = max(dp[(len1 - 1, len2)], dp[(len1, len2 - 1)])
            return dp[(len(text1),len(text2))]

        #空间压缩 左上，左边，上边三个,懒得让短的作为行了
        def f3():
            for len1 in range(1,len(text1)+1):
                leftup = 0
                for len2 in range(1,len(text2)+1):
                    tmp = row[len2]
                    if text1[len1 - 1] == text2[len2 - 1]:
                        row[len2] = leftup+1
                    else:
                        row[len2] = max(row[len2-1],row[len2])
                    leftup = tmp
            return row[len(text2)]

        return f0(len(text1), len(text2))
