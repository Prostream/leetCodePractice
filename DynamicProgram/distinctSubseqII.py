#940题
#计算一个字符串里，有多少个子序列(去掉空集)，相当于组合
#dp作为以i结尾的范围里有多少个子序列，
#遍历：
#   纯新增=all-当前的dp[i]（去掉上次加的）
#   dp[i] += 纯新增
#   all += 纯新增
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        if not s:
            return 0

        mod = 1000000007

        dp = {}
        all = 1#天生自带一个空集
        for i in range(len(s)):
            if s[i] not in dp:
                dp[s[i]] = 0
            #new = all - dp[s[i]]
            new = (all - dp[s[i]] + mod)%mod
            #dp[s[i]] += new
            dp[s[i]] = (dp[s[i]] + new)%mod
            #all += new
            all = (all + new)%mod

        #空集去掉
        return (all - 1 + mod)%mod