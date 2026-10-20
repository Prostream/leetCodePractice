def lengthOfLongestSubstring(s: str) -> int:
    #最长无重复子串
    #维护所有出现过的字符的最近位置
    map_dict = {}
    n = len(s)
    max_len = 0
    left = 0
    for i in range(n):
        c = s[i]
        if c in map_dict:
            left = max(left, map_dict[c]+1)
        max_len = max(max_len, i-left+1)

        map_dict[c] = i

    return max_len