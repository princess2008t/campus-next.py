numbers = iter(list(range(1, 101)))
while True:
    try:
        print(next(numbers))
        next(numbers)
        next(numbers)
    except StopIteration:
        break