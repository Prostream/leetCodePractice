#[1,2,1,1,3,2,5]求每个数字和它的一样的数字的位置的绝对值差值之和
from collections import defaultdict


def distance(nums):
    map_nums = defaultdict(list)
    for i in range(len(nums)):
        map_nums[nums[i]].append(i)

    #[1:0,2,3]->[1:[0,2,5]]
    res = [0]*len(nums) #答案要返回每个位置对应的绝对值差和

    for key in map_nums:
        value = sorted(map_nums[key])
        n = len(value)
        #prefix[i] -> [0,1,..,i-1]
        prefix = [0] * (n+1)
        for j in range(n):
            prefix[j+1] = prefix[j] + value[j]

        # 求和（index_i - index_(0->i-1)）+ 求和（index_last - index_(i+1 -> last)）
        for i in range(len(value)):#0,2,3
            left = i*value[i] - prefix[i]
            right =  (prefix[n] - prefix[i+1]) - (n-i-1)*value[i]
            res[value[i]] = left + right

    return res

if __name__ == "__main__":
    arr = [1, 2, 1, 1, 2, 3]
    # 期望输出: [5, 3, 3, 4, 3, 0]
    # map {[1:0,2,3], [2:1,4], [3:5]}
    # pre {[x:0,2,5], [x:1,5], [x:5]}
    print(distance(arr))