def list_of_divisors(n):
    result = []
    for i in range(2, abs(n) + 1):
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


def calculating_the_pow(num, prime_div):
    count = 0
    while num % prime_div == 0:
        count += 1
        num = num // prime_div
    return (prime_div, count)


def prime_factorization(n):
    l = list_of_divisors(n)
    l1 = [item for item in l if is_prime(item)]
    result = []
    for num in l1:
        result.append(calculating_the_pow(n, num))
    return result
