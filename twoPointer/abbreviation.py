from unicodedata import numeric


def valid_word_abbreviation(word, abbr):
    #比较心累做的
    # 2个pointer，分别指向word和abbr
    # 太多的边界条件导致算法效果不佳
    word_index, abbr_index = 0, 0
    while abbr_index < len(abbr):
        if abbr[abbr_index].isdigit():
            if abbr[abbr_index] == '0':
                return False
            num = 0
            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])#重点部分，用str手法会处理更多的边界条件
                abbr_index += 1
            word_index += num
        else:
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1
    return word_index == len(word) and abbr_index == len(abbr)
def main():
    words = ["a", "a", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "word", "internationalization",
             "localization"]
    abbreviations = ["a", "b", "a18t", "a19t", "w0rd", "i18n", "l12n"]
    for i in range(len(words)):
        print(i + 1, ".\t word: '", words[i], "'", sep="")
        print("\t abbr: ", abbreviations[i], "'", sep="")
        print(f"\n\t Is '{abbreviations[i]}' a valid abbreviation for the word '{words[i]}'? ",
              valid_word_abbreviation(words[i], abbreviations[i]), sep="")
        print("-" * 100)
if __name__ == '__main__':
    main()