def prepare_meal(number):
    count = 0
    result = ""
    while(number % 3 == 0):
        number = number // 3
        count += 1
    spams = ["spam"] * count
    result = " ".join(spams)

    if number % 5 == 0:
        if(result == ""):
            result = "eggs"
        else:
            result = result + " and eggs"

    return result
