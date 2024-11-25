#homework
class Solution:
    def prime_hash(self, strs, prime, m=100000):
        hash_value = 0
        for char in strs:
            hash_value = hash_value * prime + ord(char)  # 用质数进行累加
        #print(hash_value)
        return hash_value % m


if __name__ == '__main__':
    s = Solution()
    print(s.prime_hash("abc", 7))