def nx(n):
    prod = 1
    for x in range(1, n+1):
        prod *= x
    print(prod)
    su = 0
    for s in str(prod):
        su += int(s)
    return su

print(nx(100))
