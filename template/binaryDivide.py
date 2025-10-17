#二分答案法模板
def check(mid):
    return True

def function(nums):
    n = len(nums)
    left = 0
    right = n-1
    #如果找的是最小值，就说明最后返回的是right，因为right不断变小，这样就需要check(right)一直为真，check(left)一直为假
    while left + 1 < right:#left+1==right时跳出循环
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right

if __name__ == '__main__':
    #不好测试算了
    print("True")