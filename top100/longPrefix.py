#14
from sys import prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for str in strs[1:]:
                if i == len(str) or char != str[i]:
                    return strs[0][:i]

        return strs[0]
