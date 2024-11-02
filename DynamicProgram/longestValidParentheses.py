#26 hard
#以i结尾的子串，最长的有效括号是多少
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 0
        ans = 0
        for i in range(len(s)):
            if s[i] != '(':
                p = i - dp[i-1] - 1
                if p >= 0 and s[p] == '(':
                    dp[i] = 2 + dp[i-1] + (dp[p-1] if p>0 else 0)
            ans = max(ans, dp[i])
        return ans