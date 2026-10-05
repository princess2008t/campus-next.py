def helper(number):
    if number == 0:
        return 0
    return number % 10 + helper(number // 10)


def sum_of_digits(number):
    return helper(number)

print(sum_of_digits(104))