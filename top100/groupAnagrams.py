#49
#道题目要求将一组字符串按照字母异位词分组。字母异位词指的是由相同字母以不同顺序组成的单词
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        ans  = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
        for key in anagrams:
            ans.append(anagrams[key])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))