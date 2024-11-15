#354 俄罗斯套娃信封问题，最长递增子序列扩展
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 用宽度升序排序，如果相等用高度降序排序
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        ends = []

        # bs 用二分法来求现在这个值要放在end的哪里
        def bsf(height):
            l = 0
            r = len(ends) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if height <= ends[m]:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans

        # 求排序后的信封的以高度为准的最长严格递增子序列
        for i in range(n):
            height = envelopes[i][1]
            find = bsf(height)
            if find == -1:
                ends.append(height)
            else:
                ends[find] = height

        return len(ends)