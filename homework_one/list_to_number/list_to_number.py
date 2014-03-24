def list_to_number(digits):
    result = 0
    while digits != []:
        result = result * 10 + digits.pop(0)
    return result
