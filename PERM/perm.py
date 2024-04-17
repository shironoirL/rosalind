from itertools import permutations


def print_permutations(n):
    digits = list(range(1, n + 1))
    perm_list = list(permutations(digits))
    print(len(perm_list))
    for perm in perm_list:
        print(' '.join(map(str, perm)))

print_permutations(6)