#3
#1.中心拓展法 2.二维dp
#用方案1先,边检条件很变态这道题，背一下这个expand方法
class solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        long_str = ""
        for i in range(len(s)):
            odd = self.expand_center(i,i,s)
            if len(long_str) < len(odd):
                long_str = odd
            even = self.expand_center(i,i+1,s)
            if len(long_str) < len(even):
                long_str = even
        return long_str


    def expand_center(self, left, right, s):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

if __name__ == "__main__":
    s = solution()
    print(s.longestPalindrome("ccc"))