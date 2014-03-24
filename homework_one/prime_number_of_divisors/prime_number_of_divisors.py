def list_of_divisors(n):
    result = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)
    return result


def sum_of_divisors(n):
    result = abs(n)
    for i in range(1, abs(n)):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    return sum_of_divisors(n) == n + 1


def prime_number_of_divisors(n):
    return is_prime(len(list_of_divisors(n)))
