#happy number
def isHappy(n):
    def get_next(number):
        return sum(int(digit)**2 for digit in str(number))

    repeat = set()
    while n != 1  and n not in repeat:
        repeat.add(n)
        n = get_next(n)

    return n == 1