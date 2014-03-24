def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def simplify_fraction(fraction):
    g = gcd(fraction[0], fraction[1])
    return (fraction[0]//g, fraction[1]//g)
