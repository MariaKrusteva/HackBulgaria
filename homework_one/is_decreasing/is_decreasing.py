def is_decreasing(seq):
    count = 0
    for i in range(0, len(seq) - 1):
        if seq[i] > seq[i + 1]:
            count += 1
    return count == len(seq) - 1
