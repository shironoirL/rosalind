from itertools import product

def lexf(n):
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    perm_list = list(product(lst, repeat=n))
    for perm in perm_list:
        print(''.join(map(str, perm)))

lexf(3)
