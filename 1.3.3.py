def is_funny(string):
    return all(char in 'ha' for char in string)

print(is_funny("hahasha"))