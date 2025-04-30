#str1和str2的最大公约子串
#1.str1 + str2 == str2 + str1
#2.gcd(len(str1),len(str2)) ==> str1[:n] == str2[:n]
from math import gcd
def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    n = gcd(len(str1), len(str2))
    if str1[:n] != str2[:n]:
        return ""
    return str1[:n]

print(gcdOfStrings('ABCABC', 'ABC'))