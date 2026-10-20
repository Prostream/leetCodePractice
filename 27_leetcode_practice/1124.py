def longestWPI(hours: list[int]) -> int:
    #题意是>8小时和<=8小时
    n = len(hours)
    pre = [0] * (n+1)
    for i in range(1,n+1):
        pre[i] = pre[i-1] + (1 if hours[i-1] > 8 else -1)

    neg_dict = {}
    max_len = 0
    for i in range(1,n+1):
        cur = pre[i]
        #如果大于0，那么最长的就是
        if cur > 0:
            max_len = max(max_len, i)
        else:
            if cur-1 in neg_dict:
                max_len = max(max_len, i - neg_dict[cur-1])
            if cur not in neg_dict:
                neg_dict[cur] = i
    return max_len
