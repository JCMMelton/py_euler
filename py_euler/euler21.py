def d(n):
    a = 0
    for i in range(1, n):
        if n % i == 0:
            a += i
    return a

divisor_sums = []
total = 0
for a in range(0, 10000):
    b = d(a)
    x = d(b)
    if a == x and a != b:
        print(a, b, x, total)
        total += a

print(total)
