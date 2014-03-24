VOWELS = "aeiouyAEIOUY"


def count_vowels(str):
    sum = 0
    for vowel in VOWELS:
        sum += str.count(vowel)
    return sum
