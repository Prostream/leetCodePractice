#17
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        ans = []
        def f1(index,path):
            if index == len(digits):
                ans.append(''.join(path))
                return
            else:
                for letter in phone_map[digits[index]]:
                    path.append(letter)
                    f1(index+1,path)
                    path.pop()
        f1(0,[])
        return ans

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))