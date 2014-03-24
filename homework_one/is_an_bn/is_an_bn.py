def is_an_bn(word):
    first_half = word[:len(word)//2]
    second_half = word[len(word)//2:]
    if len(first_half) != len(second_half):
        return False
    for i in range(0, len(first_half)):
        if first_half[i] != 'a' or second_half[i] != 'b':
            return False
    return True
