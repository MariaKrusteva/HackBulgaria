COINS = [100, 50, 20, 10, 5, 2, 1]


def calculate_coins(sum):
    sum *= 100
    dict = {}
    count = 0
    for i in COINS:
        while sum >= i:
            count += 1
            sum -= i
        dict[i] = count
        count = 0
    return dict
