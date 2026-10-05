import functools
def double_letter(my_str):
    return my_str*2

print("".join(list(map(double_letter,'python'))))