def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]
    total = sum(sum(map(int, str(digit * (1 if index % 2 == 0 else 2))))for index, digit in enumerate(digits))
    return total % 10 == 0

class IDIterator:
    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        self.id_ += 1

        while self.id_ <= 999999999:
            if check_id_valid(self.id_):
                return self.id_
            self.id_ += 1
        raise StopIteration


def id_generator(id_number):
    id_number += 1
    while id_number <= 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1

# main
id_number = int(input("Enter ID: "))
choice = input("Generator or Iterator? (gen/it)? ")

if choice == "it":
    iterator = IDIterator(id_number)
    for _ in range(10):
        print(next(iterator))

elif choice == "gen":
    generator = id_generator(id_number)
    for _ in range(10):
        print(next(generator))