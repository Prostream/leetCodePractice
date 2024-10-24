#383
#判断能否从给定的杂志字符串中提取字符来构造指定的赎金信字符串。
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chr_dict = {}
        for i in range(len(ransomNote)):
            if chr_dict.get(ransomNote[i]) is None:
                chr_dict[ransomNote[i]] = 1
            else:
                chr_dict[ransomNote[i]] += 1

        for j in range(len(magazine)):
            if chr_dict.get(magazine[j]) is not None:
                chr_dict[magazine[j]] -= 1

        sum = 0
        for key in chr_dict:
            if chr_dict[key] != 0:
                return False

        return True
