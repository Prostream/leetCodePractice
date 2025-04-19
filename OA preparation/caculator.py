def caculate(s: str):
    '''递归+stack来处理+-*/
       stack = []
       1+2*(4+6)/2
       1[] num = 1
       +[1] sign="+"
       2[1,2] sign="+" num = 2
       *[1,2] sign="+" num = 0
       ([1,2] sign="*" num = 10 ——> [1,20] sign = /
       2[1,20] i=末尾 1 + 10 = 11
    '''
    n = len(s)

    def helper(s, i):
        stack = []
        num = 0
        sign = "+"
        while i < n:
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                num, i = helper(s, i + 1)

            if c == ")" or c == "+" or c == "-" or c == "*" or c == "/" or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    div = stack.pop()
                    stack.append(div / num)

                num = 0
                sign = c

                if c == ")":
                    return sum(stack), i
            i += 1
        return sum(stack), i

    return helper(s, 0)[0]


print('caculate("1+2*(12/4)")')
print(caculate("1+2*(12/4)"))

print(caculate("1+2*(4+6)/2"))
