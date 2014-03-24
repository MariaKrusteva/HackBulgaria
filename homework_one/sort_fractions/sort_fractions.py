from functools import cmp_to_key


def compare_fractions(fraction1, fraction2):
    denom = fraction1[1] * fraction2[1]
    return fraction1[0]*(denom/fraction1[1]) - fraction2[0]*(denom/fraction2[1])


def sort_fractions(fractions):
    return sorted(fractions, key=cmp_to_key(compare_fractions))
