def number_to_list(n):
    result = []
    while(n != 0):
        result.insert(0, n % 10)
        n = n // 10
    return result



