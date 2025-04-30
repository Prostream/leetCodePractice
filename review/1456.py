#定长子串中元音的最大数目
#abciiidef k=3 ans=3
def maxVowels(s,k):
    vowels = set("aeiouAEIOU")
    ans = 0
    count = 0
    # 012345678
    # abciiidef k=3
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if i >= k:
            if s[i-k] in vowels:
                count -= 1
        ans = max(ans, count)
    return ans

print(maxVowels("abciiidef",3))