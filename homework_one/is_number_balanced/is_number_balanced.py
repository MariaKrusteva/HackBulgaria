def int_to_list(n):
    result = []
    while(n != 0):
        result.append(n % 10)
        n = n // 10
    return result


def is_number_balanced(n):
    l = int_to_list(n)
    if len(l) == 1:
        return True
    elif len(l) % 2 != 0:
        return sum(l[:len(l) // 2]) == sum(l[len(l) // 2 + 1:])
    else:
        return sum(l[:len(l) // 2]) == sum(l[len(l) // 2:])
