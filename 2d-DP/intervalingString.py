#97交错字符串
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        dp = [[False for j in range(len2 + 1)] for i in range(len1 + 1)]

        if len3 != len1 + len2:
            return False

        # 子问题是，以i-1结尾的s1子串，以j-1结尾的s2子串，能不能构成前i+j长度的s3子串
        # [0...i-1] [0...j-1] => [0...i+j-1]
        # 1）from s1 s1[i-1] == s3[i+j-1]: [0...i-2]+[0...j-1] => [0...i+j-2] dp[i-1][j]
        # 2) from s2 s2[j-1] == s3[i+j-1]: dp[i][j-1]
        # 3) False
        def f1():
            dp[0][0] = True
            # i=0
            for j in range(len2 + 1):
                if s2[:j] == s3[:j]:
                    dp[0][j] = True
                else:
                    dp[0][j] = False
            for i in range(len1 + 1):
                if s1[:i] == s3[:i]:
                    dp[i][0] = True
                else:
                    dp[i][0] = False
            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    p1, p2 = False, False
                    if s1[i - 1] == s3[i + j - 1]:
                        p1 = dp[i - 1][j]
                    if s2[j - 1] == s3[i + j - 1]:
                        p2 = dp[i][j - 1]
                    dp[i][j] = p1 or p2
            return dp[len1][len2]

        return f1()



