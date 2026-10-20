def longestSubarraySum(nums: list[int], k: int) -> int:
    #题意和560一致，但是要找的是最长的子数组
    n = len(nums)
    pre = [0] *(n+1)
    for i in range(1, n+1):
        pre[i] = pre[i-1] + nums[i-1]

    first_pos= {0:0}
    max_len = 0
    for i in range(1,n+1):
        #i-->[0..i-1]
        p = pre[i]
        q = p - k
        if q in first_pos:
            max_len = max(max_len, i - first_pos[q])
        if p not in first_pos:#only log first one
            first_pos[p] = i
    return max_len