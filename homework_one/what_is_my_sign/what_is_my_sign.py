ZODIAC_TABLE = {
    (range(21, 32), 3): "Aries", (range(1, 21), 4): "Aries",
    (range(21, 31), 4): "Taurus", (range(1, 22), 5): "Taurus",
    (range(22, 32), 5): "Gemini", (range(1, 22), 6): "Gemini",
    (range(22, 31), 6): "Cancer", (range(1, 23), 7): "Cancer",
    (range(23, 32), 7): "Leo", (range(1, 23),  8): "Leo",
    (range(23, 32), 8): "Virgo", (range(1, 24), 9): "Virgo",
    (range(24, 31), 9): "Libra", (range(1, 24), 10): "Libra",
    (range(24, 32), 10): "Scorpio", (range(1, 23), 11): "Scorpio",
    (range(23, 31), 11): "Sagittarius", (range(1, 22), 12): "Sagittarius",
    (range(22, 32), 12): "Capricorn", (range(1, 21), 1): "Capricorn",
    (range(21, 31), 1): "Aquarius", (range(1, 20), 2): "Aquarius",
    (range(20, 30), 2): "Pisces", (range(1, 21), 3): "Pisces"

}


def what_is_my_sign(day, month):
    for key in ZODIAC_TABLE:
        if day in key[0] and month == key[1]:
            return ZODIAC_TABLE[key]
