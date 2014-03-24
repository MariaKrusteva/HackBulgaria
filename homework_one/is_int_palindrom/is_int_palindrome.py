def number_to_list(n):
    result = []
    while(n != 0):
        result.insert(0, n % 10)
        n = n // 10
    return result


def reverse(list):
    n = list[::-1]
    return n


def is_int_palindrome(n):
    nlist = number_to_list(n)
    nlist_Rev = reverse(nlist)
    for i in range(0, len(nlist)):
        if nlist[i] != nlist_Rev[i]:
            return False
    return True
