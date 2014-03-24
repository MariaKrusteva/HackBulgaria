def contains_digit(number, digit):
    while number != 0:
        if number % 10 == digit:
            return True
        number = number // 10
    return False


def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if contains_digit(number, digit):
            count += 1
    return count == len(digits)
