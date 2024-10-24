#392
#判断一个字符串是否为另一个字符串的子序列。
#双指针法
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pointer_s = 0
        pointer_t = 0
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        if pointer_s == len(s):
            return True
        else:
            return False
