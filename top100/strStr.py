#28
#用于在一个主字符串中找到一个子字符串的首次出现的索引。
# 如果子字符串不在主字符串中，则函数应返回 -1。这是一个经典的字符串搜索问题。
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack or not needle:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
