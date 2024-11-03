#467
#找到在s串中的子序列，在base串中也存在的，一共有多少个
#直接采用自底向顶的动态规划
#dp为，以x结尾的子串，最多有多长满足其在base串中也存在
#维护一个len，
#   如果当前的s中的当前字符的前一个字符，能够满足base串连续的规则 len += 1
#   如果不满足，len回到1
#每个字符下对应的dp[chr]的值如果小于现在的len，就更新成新的len
#结束后求和
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        length = 1
        dp = {}
        dp[s[0]] = 1
        for i in range(1, len(s)):
            chr = s[i]
            prev = s[i-1]
            if chr not in dp:
                dp[chr] = 1
            if  (chr == 'a' and prev == 'z') or ord(chr) == ord(prev) + 1:
                length += 1
            else:
                length = 1
            dp[chr] = max(length, dp[chr])
        #第一个位置不用处理，默认是1长度就行
        #求和
        ans = 0
        for key in dp:
            ans += dp[key]
        return ans
