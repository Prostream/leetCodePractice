#leetcode-1234
#You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

#A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

#Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.
#和leetcode-76是同一问题 使用负债表思路解决
import copy

def replaceSubstrForBalance(str):
     dict_str = {"Q":-(len(str)//4),"R":-(len(str)//4),"W":-(len(str)//4),"E":-(len(str)//4)}
     debt = 0
     #欠债表中可以看出哪些字符欠了多少
     for i in range(len(str)):
        #构建一个dict
        dict_str[str[i]] = dict_str[str[i]] + 1
     if dict_str["Q"] == 0 and dict_str["W"] == 0 and dict_str["E"] == 0 and dict_str["R"] == 0:
         return 0
     if dict_str["W"] > 0:
         debt = debt + dict_str["W"]
     if dict_str["E"] > 0:
         debt = debt + dict_str["E"]
     if dict_str["R"] > 0:
         debt = debt + dict_str["R"]
     if dict_str["Q"] > 0:
         debt = debt + dict_str["Q"]
     #滑动窗口寻找最短的满足要求的子串
     left = 0
     right = 0
     min_len = len(str)
     #看看进入的元素是不是多余的元素，是的话就是有效还款
     while right < len(str):
         if "Q" == str[right]:
             dict_str["Q"] = dict_str["Q"] - 1
             # 这种情况是有效的
             if dict_str["Q"] >= 0:
                 debt = debt - 1
         elif "W" == str[right]:
             dict_str["W"] = dict_str["W"] - 1
             if dict_str["W"] >= 0:
                 debt = debt - 1
         elif "E" == str[right]:
             dict_str["E"] = dict_str["E"] - 1
             if dict_str["E"] >= 0:
                 debt = debt - 1
         elif "R" == str[right]:
             dict_str["R"] = dict_str["R"] - 1
             if dict_str["R"] >= 0:
                 debt = debt - 1
         #如果还完了负债，看看能不能收缩左边的窗口边界(可以收缩掉不影响还债的)
         if debt == 0:
             while left < right:
                 #说明可以去掉这种没有影响到欠债的
                 if dict_str[str[left]] + 1 <= 0:
                     dict_str[str[left]] = dict_str[str[left]] + 1
                     left = left + 1
                 else:
                     break
             #如果有更小的子串，记录一下
             if min_len > right - left + 1:
                 min_len = right - left + 1
         right = right + 1
     return min_len

if __name__ == "__main__":
    print(replaceSubstrForBalance("WQWRQEQQWERQWWWEREWRQQWWWWQW"))

