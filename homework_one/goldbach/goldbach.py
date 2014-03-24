def sum_of_divisors(n):
    result = abs(n)
    for i in range(1, abs(n)):
        if n % i == 0:
            result += i
    return result


def is_prime(n):
    return sum_of_divisors(n) == n + 1


def primes(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


def goldbach(n):
    result = [(x, y) for x in primes(n) for y in primes(n) if x + y == n]
    for (x, y) in result:
        if (y, x) in result and x != y:
            result.remove((y, x))
    return sorted(result)
