def reduce_file_path(path):
    result = []
    for i in path.split("/"):
        if i != "." and i != "" and i != "..":
            result.append(i)
        if i == ".." and result != []:
            result.pop()
    if result == []:
        result.insert(0, "/")
    else:
        result.insert(0, "")
    return "/".join(result)
