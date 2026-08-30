class Solution:
    def calculate(self, s):
        stack = []
        sign = "+"
        num = 0
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == len(s)-1 or s[i] in ["+","-","*","/"]:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                #"1+2+3*4（4是i）"
                elif sign == "*":
                    stack[-1] *= num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
                sign = s[i]
                num = 0
        res = 0
        while stack:
            res += stack.pop()
        return res

if __name__ == "__main__":
    solution = Solution()

    print(solution.calculate("1+2+3*4"))       # 15
    print(solution.calculate("3+2*2"))         # 7
    print(solution.calculate(" 3/2 "))         # 1
    print(solution.calculate(" 3+5 / 2 "))     # 5
    print(solution.calculate("14-3/2"))         # 13