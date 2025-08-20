#完整计算器，再一次复习
def calculate(s:str):
		n = len(s)
		#递归的加入来处理括号,i表示从i位置继续处理
		#1+2*（2*4）
		def helper(s, i):
				stack = []
				num = 0
				sign = "+"
				while i < n:
						if s[i].isdigit():
								num = 10*num + int(s[i])
						if s[i] == "(":
								num, i = helper(s, i+1)
						if s[i] in "+-*/)" or i == n-1:
								if sign == "+":
										stack.append(num)
								if sign == "-":
										stack.append(-num)
								if sign == "*":
										stack[-1] = stack[-1]*num
								if sign == "/":
										stack[-1] = int(stack[-1]/num)
								sign = s[i]
								num = 0
								if s[i] == ")":
										return sum(stack), i
						i += 1
				return sum(stack),i
		return helper(s, 0)[0]

if __name__ == "__main__":
	test = ["1+2+3", "1+2*(2*4)"]
	for t in test:
		print(calculate(t))