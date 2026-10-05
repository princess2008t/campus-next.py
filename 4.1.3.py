def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_generator():
    num = 2

    while True:
        if is_prime(num):
            yield num

        num += 1
def first_prime_over(n):
    for prime in prime_generator():
        if prime > n:
            return prime


print(first_prime_over(99))