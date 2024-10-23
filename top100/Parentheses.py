#20
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:#遇到了右括号
                cur = stack.pop()
                if bracket_map[char] != cur:
                    return False
            else:#左括号
                stack.append(char)
        return not stack


