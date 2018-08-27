import itertools
dig = [x for x in range(0, 10)]
limit = 1000000
n = 0
for p in itertools.permutations(dig):
    n += 1
    if n == limit:
        print(p)
