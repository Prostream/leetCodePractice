def subarraySum(nums: list[int], k: int) -> int:
    #输入可正可负
    #寻找和为k的子数组的组合有多少
    n = len(nums)
    pre = [0] * (n+1)
    for i in range(1,n+1):
        pre[i] = pre[i-1] + nums[i-1]
    #pre[i]=[0...i-1]之和
    count = {0:1}
    result = 0
    #count 含义为值为key的前缀和出现了val次
    for i in range(1,n+1):
        pre_sum = pre[i]
        q = pre_sum - k
        if q in count:
            result += count[q]
        if pre_sum in count:
            count[pre_sum] += 1
        else:
            count[pre_sum] = 1
    return result