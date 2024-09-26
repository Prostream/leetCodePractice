#用递归函数来逆序一个栈
#
#方法 输入一个栈，输出这个栈的栈底元素，其余元素盖下
from inspect import stack

#O(n^2)时间复杂度
def reverse(stack):
    if not stack:
        return
    else:
        num = bottomOut(stack)
        reverse(stack)
        stack.append(num)
    return stack

def bottomOut(stack):
    #如果栈空，返回此时的ans
    ans = stack.pop()
    if not stack:
        return ans
    else:
        last = bottomOut(stack)
        stack.append(ans)
        return last

if __name__ == '__main__':
    stack = [1,2,3]
    print(reverse(stack))
    print(stack)