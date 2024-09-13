from re import split


def reverse_words(sentence):
    # reverse整个sentence,处理空格
    # O(n)的时间和空间复杂度
    sentence=sentence.strip()
    sentence.sub()
    split_sentence=sentence.split()
    sentence = ' '.join(split_sentence)
    sentence=sentence[::-1]
    # 初始化两个pointer start和end
    start = 0
    end = 0
    # 找到一个word，逆转start到end-1
    for i in range(len(sentence)):
        if sentence[i] == " ":
            end = i
            sentence = sentence[:start] + sentence[start:end][::-1] + sentence[end:]
            start = i+1
    #逆转最后一个单词
    sentence = sentence[:start] + sentence[start:len(sentence)][::-1]
    # 找下一个word，然后逆转
    # Replace this placeholder return statement with your code
    return sentence

# Driver code
def main():
    print(reverse_words("Hello     World"))



if __name__ == '__main__':
    main()