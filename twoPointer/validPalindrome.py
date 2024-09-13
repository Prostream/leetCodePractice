def is_palindrome(string):
    #核心在于或者的使用
    return is_palindrome_left(string) <=1 or is_palindrome_right(string) <= 1

def is_palindrome_left(string):
    # 2 pointers
    start = 0
    end = len(string) - 1
    mismatches = 0
    while start < end:
        if mismatches > 1:
            return 2
        elif string[start] != string[end]:
            mismatches = mismatches + 1
            start = start+2
            end = end-1
        else:
            start = start+1
            end = end-1
    return mismatches

def is_palindrome_right(string):
    # 2 pointers
    start = 0
    end = len(string) - 1
    mismatches = 0
    while start < end:
        if mismatches > 1:
            return 2
        elif string[start] != string[end]:
            mismatches = mismatches + 1
            start = start+1
            end = end-2
        else:
            start = start+1
            end = end-1
    return mismatches

# Driver code
def main():
    print(is_palindrome("tebbem"))

if __name__ == '__main__':
    main()