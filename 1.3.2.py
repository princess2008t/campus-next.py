def is_prime(number):
    return len([x for x in range(2, number) if number % x == 0]) == 0

print(is_prime(42))