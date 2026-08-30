#只处理加减法,且不带括号
class Solution:
    #s = "1+3-2+4"
    def calculate(s):
        #"1+3-2+4"
        #    i
        # sign = + 
        # num = 3
        # stack = [+1]  
        stack=[]
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ["+", "-"] or i == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                sign = s[i]
                num = 0
        res = 0
        while stack:
            res += stack.pop()

        return res