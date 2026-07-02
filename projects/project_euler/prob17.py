digits = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

def number_to_english(n: int) -> str:
    if n == 1000:
        return "onethousand"

    # Hundreds
    res = ""
    if n >= 100:
        a = n // 100
        res += digits[a] + "hundred"
        if n % 100:
            res += "and"
        else:
            return res
        n -= 100 * (n // 100)

    # Tens
    b = n // 10
    if b == 1:
        res += teens[n]
        return res
    elif b!= 0:
        res += tens[n // 10]

    n = n % 10
    res += digits[n]

    return res

print(sum([len(number_to_english(i)) for i in range(1, 1001)]))
