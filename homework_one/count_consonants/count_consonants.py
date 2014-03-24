def count_substrings(haystack, needle):
    return haystack.count(needle)


def count_consonants(str):
    sum = 0
    consonants = "bcdfghjklmnpqrstvwxz"
    consonants = consonants + consonants.upper()
    for letter in str:
        sum += count_substrings(consonants, letter)
    return sum
