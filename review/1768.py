def mergeAlternately(word1, word2):
    p1 = 0
    p2 = 0
    word_turn = 1
    ans = []
    while p1 < len(word1) and p2 < len(word2):
        if word_turn == 1:
            ans.append(word1[p1])
            p1 += 1
            word_turn = 2
        elif word_turn == 2:
            ans.append(word2[p2])
            p2 += 1
            word_turn = 1
    if p1 == len(word1):
        ans.append(word2[p2:])
    elif p2 == len(word2):
        ans.append(word1[p1:])

    return "".join(ans)

print(mergeAlternately("abc", "pqr"))