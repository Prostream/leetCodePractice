def is_happy_number(n):
    # fast pointer and slow pointer
    fast = n
    slow = n
    #
    if n == 1:
      return True
    while fast != 1:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False
    return False

def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum