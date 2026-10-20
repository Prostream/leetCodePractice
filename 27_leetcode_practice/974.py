def subarraysDivByK(nums: list[int], k: int) -> int:
    #
    n = len(nums)
    pre = [0] * (n+1)
    for i in range(1,n+1):
        pre[i] = pre[i-1] + nums[i-1]
    # p % k = q % k
    mod_dict = {0:1}
    result = 0
    for i in range(1,n+1):
        val = pre[i] % k
        if val in mod_dict:
            result += mod_dict[val]
            mod_dict[val] += 1
        else:
            mod_dict[val] = 1

    return result