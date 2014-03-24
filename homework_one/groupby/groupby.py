def groupby(func, seq):
    result = {}
    for num in seq:
        if not func(num) in result:
            result[func(num)] = [num]
        else:
            result[func(num)].append(num)
    return result
