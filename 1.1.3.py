def helper(number):
    if number == 0:
        return []
    result = helper(number - 1)
    if number % 4 == 0:
        result.append(number)
    return result


def four_dividers(number):
    return helper(number)

print(four_dividers(9))