#474
#str是一个字符串构成的list["10","0001","111001","1","0"]
#求出str能取出最多的元素个数，满足0的个数小于m,1的个数小于n
import functools
from collections import defaultdict
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp = defaultdict(int)

        # 暴力递归
        # 从[i...]，0小于等于z，1小于等于O，最多取到的元素个数
        @functools.cache
        def f0(i, z, o):
            # 越界,只能取到0个
            if i >= len(strs):
                return 0
            # 可能性1，i这个位置的字符串，在最后结果中不使用
            p1 = f0(i + 1, z, o)
            p2 = 0
            zero = strs[i].count('0')
            one = strs[i].count('1')
            # 可能性2，i这个位置的字符串，在最后结果中要使用
            if z - zero >= 0 and o - one >= 0:
                p2 = 1 + f0(i + 1, z - zero, o - one)
            return max(p1, p2)

        # 记忆化搜索
        def f1(i, z, o):
            if (i, z, o) in dp:
                return dp[(i, z, o)]
            # 越界,只能取到0个
            if i >= len(strs):
                dp[(i, z, o)] = 0
                return 0
            # 可能性1，i这个位置的字符串，在最后结果中不使用
            p1 = f1(i + 1, z, o)
            p2 = 0
            zero = strs[i].count('0')
            one = strs[i].count('1')
            # 可能性2，i这个位置的字符串，在最后结果中要使用
            if z - zero >= 0 and o - one >= 0:
                p2 = 1 + f1(i + 1, z - zero, o - one)
            dp[(i, z, o)] = max(p1, p2)
            return dp[(i, z, o)]

        # 空间压缩
        def f3():
            dpplat = defaultdict(int)  # 默认值0
            for i in range(len(strs)):
                zero = strs[i].count('0')
                one = strs[i].count('1')
                for z in range(m, -1, -1):
                    for o in range(n, -1, -1):
                        if z - zero >= 0 and o - one >= 0:
                            dpplat[(z, o)] = max(dpplat[(z, o)], 1 + dpplat[(z - zero, o - one)])
                # for z in range(m+1):
                #     print("\n")
                #     for o in range(n+1):
                #         print(f"{dpplat[(z,o)]}", end=" ")
                # print("\n")
                # print("==========")
            return dpplat[(m, n)]

        # 空间压缩 别用dict了
        def f4():
            dp_2d = [[0 for i in range(n + 1)] for j in range(m + 1)]
            for i in range(len(strs)):
                zero = strs[i].count('0')
                one = strs[i].count('1')
                for z in range(m, -1, -1):
                    for o in range(n, -1, -1):
                        if z - zero >= 0 and o - one >= 0:
                            dp_2d[z][o] = max(dp_2d[z][o], 1 + dp_2d[z - zero][o - one])
            return dp_2d[m][n]

        # return f0(0,m,n)
        # return f3()
        return f4()
