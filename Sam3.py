from collections import Counter

def top_three_digits(digit_string):
    count = Counter(digit_string)

    most_common = count.most_common(3)

    result = {int(key): value for key, value in most_common}

    return dict(sorted(result.items()))


digit_string = "123456789012345678901234567890"
result = top_three_digits(digit_string)
print(result)

