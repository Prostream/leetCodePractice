from xmlrpc.client import MAXINT


def min_window(str1, str2):
    #str1="abbcd" str2="ac" return="abbc"
    #两个指针指向0，如果相等，一起移动，如果不等，只移动str1的指针
    #当str2的指针结束了，保存这个str1的子序列，如何把str1的指针指向下一个位置，重新开找
    index_str1 = 0
    index_str_l = 0
    index_str2 = 0
    min_sub_str = ""
    min_sub_len = float('inf')
    while index_str1 < len(str1):
        if str1[index_str1] == str2[index_str2]:
            if index_str2 == 0:
                index_str_l = index_str1
            index_str1 = index_str1 + 1
            index_str2 = index_str2 + 1
        else:
            index_str1 = index_str1 + 1
        if index_str2 == len(str2):
            #如果现在的长度更短保存此时的str1子序列
            if min_sub_len > index_str1 - index_str_l + 1:
                min_sub_str = str1[index_str_l:index_str1]
                min_sub_len = len(min_sub_str)
            index_str2 = 0
    return min_sub_str

# driver code
def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["bde", "kzed", "css", "la", "ab"]

    # let's uncomment the following test case and verify the result
    # str1.append("abcdedeaqdweq")
    # str2.append("aqeq")

    for i in range(len(str1)):
        print(i + 1, ". \tInput string: (" + str1[i] + ", " + str2[i] + ")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-" * 100)
    #min_window("zxcvnhss", "css")


if __name__ == '__main__':
    main()