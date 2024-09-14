def find_repeated_sequences(dna, k):
    # 遍历dna，k长度的子序列
    set_res = set()
    set_hash = set()
    for i in range(len(dna) - k + 1):
        hash_k = hash(dna[i:i+k])
        if hash_k in set_hash:
            set_res.add(dna[i:i+k])
        set_hash.add(hash_k)
    # 记录其中子序列的hash值
    # 如果遇到的子序列的hash值已被记录过，在返回set中加入这个子序列

    return set_res

# Driver
def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print()
        print(find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()