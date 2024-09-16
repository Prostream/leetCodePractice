#leetcode-76
#返回str2在str1中找到的最小子串，包含str2里的所有字符，个数也要一致，顺序无所谓
def minWindow(str1, str2):
    # 维护一张欠债表 debt = []，如果str2中某个字符需要被囊括几次，视为几次欠债，str1中不在str2的值，是为无效还款
    start = 0
    length = 1000000000000000000000000
    debt_tbl = [0] * 255
    if len(str2) > len(str1):
        return ""
    # 为需要被囊括的字符设置好欠债
    for char in str2:
        debt_tbl[ord(char)] = debt_tbl[ord(char)] - 1
    debt = len(str2)
    l = 0
    # 以i结尾的子串，能不能完成还款
    for i in range(len(str1)):
        debt_tbl[ord(str1[i])] = debt_tbl[ord(str1[i])] + 1
        if debt_tbl[ord(str1[i])] <= 0:
            # 有效还钱
            debt = debt - 1
        if debt == 0:
            # 还清了，可以开始收缩左边界了
            while debt_tbl[ord(str1[l])] > 0:
                debt_tbl[ord(str1[l])] = debt_tbl[ord(str1[l])] - 1
                l = l + 1
            if length > i - l + 1:
                start = l
                length = i - l + 1
    if length == 1000000000000000000000000:
        return ""
    return str1[start:start + length]

if __name__ == '__main__':
    #print(ord("a"))
    print(minWindow("a","b"))