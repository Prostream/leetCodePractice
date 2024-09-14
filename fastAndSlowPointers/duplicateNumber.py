def find_duplicate(nums):
    # [1，2，3，4，5，6，7] 重点是，只有一个重复的数，且n+1个数，分布在1-n的区间
    # 这里有个把数组理解为链表的思想，这个问题就被类比成了链表中的环问题，找到环的终点，然后找到环的起点，就是我们要的重复数字
    slow = 0
    fast = 0
    while slow == 0 or slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        if slow == fast:
            #找到了终点,开始寻找起点
            slow2 = 0
            while slow2 == 0 or slow2 != slow:
                slow2 = nums[slow2]
                slow = nums[slow]
                if slow == slow2:
                    return slow
    return 0
