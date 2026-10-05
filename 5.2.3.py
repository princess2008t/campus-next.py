from itertools import combinations_with_replacement
bills = [20, 10, 5, 1]
limits = [3, 5, 2, 5]
solutions = []
for length in range(1, 16):
    for combination in combinations_with_replacement(bills, length):
        if combination.count(20) <= 3 and \
           combination.count(10) <= 5 and \
           combination.count(5) <= 2 and \
           combination.count(1) <= 5:

            if sum(combination) == 100:
                solutions.append(combination)

for solution in solutions:
    print(solution)

print("number of solutions", len(solutions))