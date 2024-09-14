def circular_array_loop(nums):
    #O(N^2)时间复杂度，O（1）空间复杂度
    # 这里的的arrayloop定义很复杂：1.loop的方向只能同向 2.不能是一个元素的自循环
    # 两个pointer
    #对每一个index作为起点进行一次找环操作，如果fast的下一个元素是自己，或者过程中改变了方向，return false
    for i in range(len(nums)):
        slow = i
        fast = i
        #得是同方向的 且 不能是一个元素的自循环
        while True:
            slow = next_index(slow, nums)
            fast = next_index(fast, nums)
            fast = next_index(fast, nums)
            #这里判断的后置很重要，需要走一步再看看是不是在自循环
            if nums[i]*nums[fast] < 0 or nums[i]*nums[slow] < 0:
                break
            if fast == next_index(fast, nums) or slow == next_index(slow, nums):
                break
            if fast == slow:
                return True
    return False

def next_index(i, nums):
    #取模法构建循环array
    return (i + nums[i]) % len(nums)

# Driver code
def main():

    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()

