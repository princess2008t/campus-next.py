def parse_ranges(ranges_string):
    first_generator = (item.split('-') for item in ranges_string.split(','))
    second_generator = (num for start, stop in first_generator for num in range(int(start), int(stop) + 1))
    return second_generator



print(list(parse_ranges("1-2,4-4,8-10")))