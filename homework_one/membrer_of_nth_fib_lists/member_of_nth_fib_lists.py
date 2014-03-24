def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    return nth_fib_lists(listB, listA + listB, n-1)


def member_of_nth_fib_lists(listA, listB, needle):
    i = 1
    result = []
    while len(result) < len(needle):
        result = nth_fib_lists(listA, listB, i)
        i += 1
    return result == needle
