def unique_words_count(arr):
    result = []
    for word in arr:
        if not word in result:
            result.append(word)
    return len(result)
