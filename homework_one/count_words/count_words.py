def count_words(arr):
    dictionary = {}
    for i in range(0, len(arr)):
        dictionary[arr[i]] = arr.count(arr[i])
    return dictionary
