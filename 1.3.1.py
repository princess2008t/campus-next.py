def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))

print(intersection([1,3,2,3],[1,2,4,5,5]))