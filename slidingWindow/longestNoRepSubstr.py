#找一个str里最长的无重复字符的字串
#leetcode-3
#"aasdsssssbcccccdaa"--->3 asd sbc cda
def longest_no_rep_substr(str):
    #用i结尾的最长的滑动窗口是，做边界=MAX（左边界，重复字符位置+1）
    left = 0
    chr_dict = {}
    sub_str = ""
    sub_str_max_len = 0
    for i in range(len(str)):
        #如果有重复的字符，收缩左边界
        if str[i] in sub_str:
            left = max(left, chr_dict.get(str[i])+1)
        sub_str = str[left:i+1]
        #保存sub_str中每个字符在str里的index
        chr_dict[str[i]] = i
        #如果此时的子序列是最长的，保存起来
        sub_str_max_len = max(len(sub_str), sub_str_max_len)

    return sub_str_max_len