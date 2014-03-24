def sum_of_divisors(n):
    result = abs(n)
    for i in range(1, abs(n)):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    return sum_of_divisors(n) == n + 1
