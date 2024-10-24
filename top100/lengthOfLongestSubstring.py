#3
#最长的无重复字符的子串的长度。
class Solution(object):
    def lengthOfLongestSubstring(self, str):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        chr_dict = {}
        max_len = 0
        sub_str = ""
        for r in range(len(str)):
            #如果r是重复值，收缩左边界至不重复
            if str[r] in chr_dict:
                left = max(left, chr_dict[str[r]]+1)
            sub_str = str[left:r+1]
            chr_dict[str[r]] = r
            if len(sub_str) > max_len:
                max_len = len(sub_str)
        return max_len