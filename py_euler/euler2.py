def fibo(l):
    a = b = 1
    for n in range(0, l):
        yield a
        a, b = b, a + b


def even(n):
    return n if n % 2 == 0 else 0

sum = 0
for i in fibo(100):
    if i > 4000000:
        break
    sum += even(i)

print(sum)
